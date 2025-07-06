#!/usr/bin/env python3
"""
Test script for Academic Video Finder
"""

import unittest
import tempfile
import os
from app import app, extract_topics_from_text, search_youtube_videos

class TestAcademicVideoFinder(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_page(self):
        """Test that the home page loads correctly"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Academic Video Finder', response.data)
    
    def test_topic_extraction(self):
        """Test topic extraction functionality"""
        sample_text = """
        Chapter 1: Introduction to Database Management Systems
        This chapter covers the basic concepts of DBMS.
        
        Section 2: Relational Model
        - Primary Keys
        - Foreign Keys
        - Normalization
        
        Unit 3: SQL Queries
        1. SELECT statements
        2. JOIN operations
        3. Aggregation functions
        """
        
        topics = extract_topics_from_text(sample_text)
        self.assertIsInstance(topics, list)
        self.assertGreater(len(topics), 0)
        
        # Check if some expected topics are extracted
        topics_text = ' '.join(topics).lower()
        self.assertIn('database', topics_text)
    
    def test_youtube_search(self):
        """Test YouTube search functionality"""
        # Test with a simple academic topic
        videos = search_youtube_videos("database management systems", max_results=3)
        
        # Should return a list (might be empty if no connection)
        self.assertIsInstance(videos, list)
        
        # If videos are found, check structure
        if videos:
            video = videos[0]
            self.assertIn('title', video)
            self.assertIn('url', video)
            self.assertIn('channel', video)
    
    def test_api_search_endpoint(self):
        """Test the API search endpoint"""
        response = self.app.post('/api/search', 
                                json={'query': 'machine learning', 'max_results': 2},
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('videos', data)
        self.assertIsInstance(data['videos'], list)
    
    def test_file_upload_no_file(self):
        """Test file upload with no file"""
        response = self.app.post('/upload', data={})
        # Should redirect back to home page
        self.assertEqual(response.status_code, 302)

def run_integration_test():
    """Run a simple integration test"""
    print("Running integration test...")
    
    # Test topic extraction
    sample_academic_text = """
    Introduction to Machine Learning
    
    Chapter 1: Supervised Learning
    - Linear Regression
    - Logistic Regression
    - Decision Trees
    - Random Forest
    
    Chapter 2: Unsupervised Learning
    - K-Means Clustering
    - Hierarchical Clustering
    - Principal Component Analysis
    
    Chapter 3: Neural Networks
    - Perceptron
    - Multi-layer Perceptrons
    - Backpropagation Algorithm
    """
    
    print("Testing topic extraction...")
    topics = extract_topics_from_text(sample_academic_text)
    print(f"Extracted {len(topics)} topics:")
    for i, topic in enumerate(topics[:5], 1):
        print(f"  {i}. {topic}")
    
    if topics:
        print("\nTesting YouTube search...")
        first_topic = topics[0]
        videos = search_youtube_videos(first_topic, max_results=2)
        print(f"Found {len(videos)} videos for '{first_topic}':")
        for video in videos:
            print(f"  - {video['title']} by {video['channel']}")
    
    print("\nIntegration test completed!")

if __name__ == '__main__':
    print("Academic Video Finder - Test Suite")
    print("=" * 40)
    
    # Run integration test
    try:
        run_integration_test()
        print("\n" + "=" * 40)
        print("✓ Integration test passed!")
    except Exception as e:
        print(f"\n✗ Integration test failed: {e}")
    
    # Run unit tests
    print("\nRunning unit tests...")
    unittest.main(argv=[''], exit=False, verbosity=2)
