# Flask Error Pages :computer:

Welcome to `flask-error-pages`! This repository provides customizable error pages by Flask applications, making it easy to maintain a seamless user experience even when things go wrong.

## About The Project

`flask-error-pages` is a dynamic version of [static-error-pages](https://github.com/bamboobyyte/static-error-pages), designed to integrate easily into Flask applications. With this project, you can customize your error pages (like 404, 500, etc.) to fit the style and tone of your application.

### Features

- 📄 Customizable error pages for common HTTP errors
- 📐 Dynamic content rendering from configuration files
- ⚙️ Easy integration with Flask applications

## Getting Started :rocket:

To use `flask-error-pages` in your Flask application, follow these steps:

### Prerequisites

It's recommended to use a virtual environment for Python projects to avoid dependency conflicts. You can set up a virtual environment using:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `.\venv\Scripts\activate.ps1`
```

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/bamboobyyte/flask-error-pages.git
cd flask-error-pages
```

2. **Install the required packages:**

```bash
pip install -r requirements.txt
```

### Configuration

Edit the data.yaml file to change the title and paragraph text for the error pages as needed.

### Running the Application

To run the application and see your error pages in action:

```bash
python app.py
```

Now, navigate to http://127.0.0.1:5000/ in your web browser. To trigger different error pages, try accessing routes that do not exist or simulate server errors.

## Contributing :handshake:

Contributions to `flask-error-pages` are welcome! If you have suggestions or improvements, feel free to fork the repo and submit a pull request.

## License :page_facing_up:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
