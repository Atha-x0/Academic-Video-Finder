"""
Configuration file for Academic Video Finder
"""

import os

class Config:
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-this-in-production'
    
    # File upload configuration
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'pdf', 'ppt', 'pptx'}
    
    # YouTube search configuration
    MAX_VIDEOS_PER_TOPIC = 5
    MAX_TOPICS_TO_EXTRACT = 10
    
    # Topic extraction configuration
    MIN_TOPIC_LENGTH = 10  # Minimum characters for a topic
    MAX_TOPIC_LENGTH = 100  # Maximum characters for a topic
    
    # Academic keywords for better topic extraction
    ACADEMIC_KEYWORDS = [
        'introduction', 'concept', 'theory', 'principle', 'method', 'approach',
        'algorithm', 'technique', 'framework', 'model', 'system', 'process',
        'analysis', 'implementation', 'application', 'example', 'case study',
        'definition', 'overview', 'fundamentals', 'basics', 'advanced',
        'architecture', 'design', 'development', 'evaluation', 'comparison'
    ]
    
    # Chapter/section patterns for topic extraction
    CHAPTER_PATTERNS = [
        r'chapter\s+\d+[:\-\s]+([^\n\.]+)',
        r'section\s+\d+[:\-\s]+([^\n\.]+)',
        r'unit\s+\d+[:\-\s]+([^\n\.]+)',
        r'topic\s+\d+[:\-\s]+([^\n\.]+)',
        r'lecture\s+\d+[:\-\s]+([^\n\.]+)',
        r'part\s+\d+[:\-\s]+([^\n\.]+)',
        r'module\s+\d+[:\-\s]+([^\n\.]+)'
    ]
    
    # Bullet point patterns for topic extraction
    BULLET_PATTERNS = [
        r'•\s*([^\n•]+)',
        r'\d+\.\s*([^\n\d]+)',
        r'-\s*([^\n-]+)',
        r'\*\s*([^\n\*]+)'
    ]

class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-must-set-a-secret-key-in-production'

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
