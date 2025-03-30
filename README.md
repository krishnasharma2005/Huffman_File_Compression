# 📂 Huffman File Compressor

A web-based file compression tool using Huffman Encoding. Upload a text file, compress it efficiently, and download the compressed version (in bits) while preserving the original content.

## 🚀 Features
- Compresses text files using Huffman Encoding.
- Displays binary format of text before download.
- Shows percentage reduction in file size.
- Clean and user-friendly interface.
- Works entirely in the browser with a Python backend.

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Algorithm:** Huffman Coding

## 🎯 How It Works
1. Upload a `.txt` file.
2. The Huffman algorithm encodes the file, reducing its size.
3. The binary format and percentage reduction are displayed.
4. Download the compressed file.

## 🏗️ Setup and Installation
### Prerequisites
- Python 3.x installed
- Flask installed (`pip install flask flask_cors`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/huffman-file-compressor.git
   cd huffman-file-compressor

2. Run the backend:
   ```bash
   python server.py

## 📝 Future Improvements
- Support for multiple file formats.
- Add decmpression functionality.
- Enhance UI for animations.
