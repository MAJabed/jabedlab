---
permalink: /
title: "Material Discovery Group at UDC"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

------

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Two Column Layout</title>
  <style>
    .container {
      display: flex;
      width: 100%;
      max-width: 1000px;
      margin: 0 auto;
      border: none #1px solid #ccc;
    }

    .left-column,
    .right-column {
      vertical-align: top;
      padding: 12px;
      font-size: clamp(14px, 1.2vw, 18px);
      #line-height: 0.4;
      white-space: normal;
      word-wrap: break-word;
      box-sizing: border-box;
    }  

    .container .left {
     flex: 1;  /* 1/3 of total */
     }

    .container .right {
      white-space: normal;
      word-wrap: break-word;
      flex: 2;  /* 2/3 of total */
    }


    .left-column {
      display: flex;
      align-items: right; #center;
      justify-content: right #center;
      background-color: #fafbfc;
    }

    .left-column img {
      max-width: 100%;
      height: auto;
      object-fit: cover;
    }
    
    .name {
      font-size: 1.80rem;
#      font-weight: bold;
      white-space: normal;
      word-wrap: break-word;
      }

    .right-column {
      background-color: #fafbfc;
      line-height: 1.2
    }
  </style>
</head>
<body>

  <div class="container">
    <div class="left-column">
      <img src="images/Jabed_Mohammed.jpg" width="200" alt="Dr. Jabed">
    </div>
    <div class="right-column">
      <p class="name" style="font-weight: bold; font-size: 20px; line-height: 0.5" >Mohammed A. Jabed, Ph.D.</p>
      <p class="name" >
      Assistant Professor<br>
      Department of Chemistry<br>
      University of the District of Columbia<br>
      Washington, DC-20002<br>
      <br><br> 
      Email: mohammed.jabed@udc.edu<br>
      Phone: (202) 274-7274 <br>
      Office: Building 44, Room: 203, Suite: 04 
      </p>
    </div>
  </div>
</body>
------

