from flask import Flask, request
import requests
  from time import sleep
  import time
  from datetime import datetime
  app = Flask(__name__)
  app.debug = True
  
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prince Onfire</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <html>
    <head>
        <style>
        body {
        background-image: url('https://i.postimg.cc/FsmmkkW2/IMG-20241201-WA0015.jpg');
        background-size: cover;
    }
    body {
      font-family: Arial, sans-serif;
    }
    
    .container {
      width: 300px;
      margin: 0 auto;
      margin-top: 100px;
      border: 1px solid #ccc;
      padding: 20px;
    }
    
    .container label, .container input[type="text"], .container input[type="password"] {
      display: black;
      width: 100%;
      margin-bottom: 10px;
    }
    
    .container button {
      width: 100%;
      padding: 10px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }

    .container button:hover {
      background-color: #55a049;
    }
  </style>
    </head>
    <body>
  <header class="header mt-4">    <h1 class="mb-3" style="color: red;"> (-𝗧𝗛𝟯 𝗟𝟯𝗚𝟯𝗡𝗗 𝗕𝗢𝗬 𝗩𝗜𝗩𝟯𝗞 𝗧𝗢𝗠𝟰𝗥-)</h1>
    <h1 class="mt-3" style="color: White;"> (-𝗛𝗘𝗔𝗧𝗘𝗥𝗦 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗡𝗘 𝗪𝗔𝗟𝗔 𝗩𝗜𝗩𝗘𝗞 𝗧𝗢𝗠𝗔𝗥-)</h1>
    <h1 class="mt-3" style="color: cyan;"> (- 𝗙𝗘𝗘𝗟 𝗧𝗛𝗘 𝗣𝗢𝗪𝗘𝗥 𝗢𝗥 𝗩𝗜𝗩𝗘𝗞 𝗧𝗢𝗠𝗔𝗥 -)
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">Enter Your Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by 𝗩𝗶𝘃𝗲𝗸 𝗧𝗼𝗺𝗮𝗿  𝟮𝟬𝟮𝟱. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <p>Keep enjoying  <a href="https://github.com/</a></p>
  </footer>
</body>
  </html>
