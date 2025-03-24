function uploadFile() {
    let fileInput = document.getElementById("fileInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select a file first!");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/compress", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        let formattedBinary = formatBinary(data.encoded_text);

        document.getElementById("result").innerHTML = `
            <div class="info-box">
                <p>📂 <strong>Original Size:</strong> ${data.original_size} bytes</p>
                <p>🗜 <strong>Compressed Size:</strong> ${data.compressed_size} bytes</p>
                <p>📉 <strong>Compression:</strong> ${data.compression_percentage}% Reduction</p>
            </div>

            <div class="compressed-box">
                <p><strong>🔎 Binary Preview:</strong></p>
                <pre id="binaryPreview">${formattedBinary}</pre>
                <button onclick="copyText()">📋 Copy</button>
            </div>

            <a class="download-btn" href="http://127.0.0.1:5000/download" download="compressed.bin">📥 Download Binary Preview</a>
        `;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerHTML = `<p style="color:red;">❌ JavaScript Error: Failed to fetch</p>`;
    });
}

function formatBinary(binaryText) {
    return binaryText.match(/.{1,50}/g).join("\n"); // Break into 50-bit lines
}

function copyText() {
    let binaryText = document.getElementById("binaryPreview").innerText;
    navigator.clipboard.writeText(binaryText).then(() => {
        alert("Copied to clipboard!");
    });
}
