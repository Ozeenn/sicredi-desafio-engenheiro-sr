app_style = '''
    <style>
        .stApp {
            background-color: #3FA110;
        }
        section[data-testid="stSidebar"] {
            background-color: white;
            color: #146E37;
        }
        section[data-testid="stSidebar"] * {
            color: #146E37 !important;
        }
        .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span {
            color: white;
        }
        .css-ng1t4o {
            box-shadow: none !important;
            border: none !important;
        }
        header[data-testid="stHeader"], footer {
            background-color: #3FA110;
        }  
        input[type="text"] {
            background-color: #5A645A;
            color: white;
            border: 1px solid black;
            border-radius: 6px;
        }
        input[type="text"]::placeholder {
            color: #cccccc;
        }
        div.stButton > button {
            background-color: #5A645A;
            color: white;
            border: 2px solid black;
            border-radius: 6px;
        }
        div.stButton > button:hover {
            background-color: #4A544A;
        }
        .stProgress > div > div > div > div {
            background-color: #FFCD00 !important;
        }
        div[data-testid="stDownloadButton"] > button {
            background-color: #5A645A;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1.2rem;
            font-size: 1rem;
            font-weight: 600;
            transition: 0.3s ease;
        }

        div[data-testid="stDownloadButton"] > button:hover {
            background-color: #3F4A3F;
            cursor: pointer;
        }

    </style>
'''