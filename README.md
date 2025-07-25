# Academic Video Finder

A web platform that extracts content from academic PDF and PowerPoint files and finds relevant YouTube videos for each topic.

## Features

- **Document Processing**: Supports PDF and PowerPoint (.ppt, .pptx) files
- **Intelligent Topic Extraction**: Automatically identifies key topics from your study materials
- **YouTube Integration**: Finds relevant educational videos for each extracted topic
- **Clean UI**: Modern, responsive interface with Bootstrap
- **Custom Search**: Search for additional videos on any topic
- **Real-time Results**: Get instant video recommendations

## How It Works

1. **Upload**: Upload your PDF or PowerPoint study material
2. **Extract**: The system extracts text and identifies key topics using pattern matching
3. **Search**: Automatically searches YouTube for relevant educational videos
4. **Display**: Shows organized results with video thumbnails, titles, and links

## Installation

1. **Clone/Download** the project files
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to `http://localhost:5000`

3. **Upload a file**: Click on the upload area and select your PDF or PowerPoint file

4. **View results**: The platform will automatically extract topics and find relevant YouTube videos

## Example Use Cases

- **DBMS Course**: Upload a database management systems PowerPoint → Get videos about SQL, normalization, indexing, etc.
- **Machine Learning**: Upload ML lecture notes → Get videos about algorithms, neural networks, data preprocessing
- **Operating Systems**: Upload OS concepts PDF → Get videos about processes, memory management, file systems

## Technical Details

### Topic Extraction
The system uses multiple approaches to extract topics:
- **Pattern Recognition**: Looks for chapter/section headers, bullet points, numbered lists
- **Keyword Analysis**: Identifies academic terminology and concepts
- **Sentence Analysis**: Extracts meaningful sentences with educational keywords

### YouTube Search
- Uses the `youtube-search` library for video discovery
- Searches for educational content related to each extracted topic
- Provides video metadata including title, channel, duration, and view count

### File Processing
- **PDF**: Uses PyPDF2 for text extraction
- **PowerPoint**: Uses python-pptx for slide content extraction
- **Security**: Files are processed and immediately deleted for privacy

## Configuration

### Secret Key
Change the secret key in `app.py` for production use:
```python
app.secret_key = 'your-secure-secret-key-here'
```

### Upload Limits
Current file size limit is 16MB. Modify in `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

## API Endpoints

### Upload Document
- **POST** `/upload`
- Accepts multipart/form-data with file upload
- Returns HTML results page

### Search Videos
- **POST** `/api/search`
- Accepts JSON: `{"query": "topic", "max_results": 5}`
- Returns JSON: `{"videos": [...]}`

## File Structure

```
academic-video-finder/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Upload page
│   └── results.html      # Results page
└── uploads/              # Temporary upload directory
```

## Dependencies

- **Flask**: Web framework
- **PyPDF2**: PDF processing
- **python-pptx**: PowerPoint processing
- **youtube-search**: YouTube video search
- **Werkzeug**: File handling utilities
- **requests**: HTTP requests

## Browser Support

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install dependencies with `pip install -r requirements.txt`
2. **File upload fails**: Check file size (max 16MB) and format (PDF, PPT, PPTX only)
3. **No videos found**: Try documents with clearer topic structure or use custom search
4. **YouTube search fails**: Check internet connection

### Performance Tips

- Use documents with clear headings and structure for better topic extraction
- Smaller files (under 5MB) process faster
- PDF files with good text content work better than scanned images

## Future Enhancements

- Support for more file formats (Word documents, text files)
- Advanced NLP for better topic extraction
- Video quality scoring and ranking
- User accounts and saved searches
- Integration with other video platforms
- Mobile app version

## License

This project is open source and available under the MIT License.
## Academic Video Finder

A web platform that extracts content from academic PDF and PowerPoint files and finds relevant YouTube videos for each topic.

## Features

- **Document Processing**: Supports PDF and PowerPoint (.ppt, .pptx) files
- **Intelligent Topic Extraction**: Automatically identifies key topics from your study materials
- **YouTube Integration**: Finds relevant educational videos for each extracted topic
- **Clean UI**: Modern, responsive interface with Bootstrap
- **Custom Search**: Search for additional videos on any topic
- **Real-time Results**: Get instant video recommendations

## How It Works

1. **Upload**: Upload your PDF or PowerPoint study material
2. **Extract**: The system extracts text and identifies key topics using pattern matching
3. **Search**: Automatically searches YouTube for relevant educational videos
4. **Display**: Shows organized results with video thumbnails, titles, and links

## Installation

1. **Clone/Download** the project files
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to `http://localhost:5000`

3. **Upload a file**: Click on the upload area and select your PDF or PowerPoint file

4. **View results**: The platform will automatically extract topics and find relevant YouTube videos

## Example Use Cases

- **DBMS Course**: Upload a database management systems PowerPoint → Get videos about SQL, normalization, indexing, etc.
- **Machine Learning**: Upload ML lecture notes → Get videos about algorithms, neural networks, data preprocessing
- **Operating Systems**: Upload OS concepts PDF → Get videos about processes, memory management, file systems

## Technical Details

### Topic Extraction
The system uses multiple approaches to extract topics:
- **Pattern Recognition**: Looks for chapter/section headers, bullet points, numbered lists
- **Keyword Analysis**: Identifies academic terminology and concepts
- **Sentence Analysis**: Extracts meaningful sentences with educational keywords

### YouTube Search
- Uses the `youtube-search` library for video discovery
- Searches for educational content related to each extracted topic
- Provides video metadata including title, channel, duration, and view count

### File Processing
- **PDF**: Uses PyPDF2 for text extraction
- **PowerPoint**: Uses python-pptx for slide content extraction
- **Security**: Files are processed and immediately deleted for privacy

## Configuration

### Secret Key
Change the secret key in `app.py` for production use:
```python
app.secret_key = 'your-secure-secret-key-here'
```

### Upload Limits
Current file size limit is 16MB. Modify in `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

## API Endpoints

### Upload Document
- **POST** `/upload`
- Accepts multipart/form-data with file upload
- Returns HTML results page

### Search Videos
- **POST** `/api/search`
- Accepts JSON: `{"query": "topic", "max_results": 5}`
- Returns JSON: `{"videos": [...]}`

## File Structure

```
academic-video-finder/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Upload page
│   └── results.html      # Results page
└── uploads/              # Temporary upload directory
```

## Dependencies

- **Flask**: Web framework
- **PyPDF2**: PDF processing
- **python-pptx**: PowerPoint processing
- **youtube-search**: YouTube video search
- **Werkzeug**: File handling utilities
- **requests**: HTTP requests

## Browser Support

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install dependencies with `pip install -r requirements.txt`
2. **File upload fails**: Check file size (max 16MB) and format (PDF, PPT, PPTX only)
3. **No videos found**: Try documents with clearer topic structure or use custom search
4. **YouTube search fails**: Check internet connection

### Performance Tips

- Use documents with clear headings and structure for better topic extraction
- Smaller files (under 5MB) process faster
- PDF files with good text content work better than scanned images

## Future Enhancements

- Support for more file formats (Word documents, text files)
- Advanced NLP for better topic extraction
- Video quality scoring and ranking
- User accounts and saved searches
- Integration with other video platforms
- Mobile app version

## License

This project is open source and available under the MIT License.
#
