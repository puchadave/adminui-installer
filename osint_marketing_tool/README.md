# OSINT Marketing Tool

## Overview
The OSINT Marketing Tool is a modular, multi-tenant business framework built on Flask. It integrates various functionalities such as user management, tenant management, and AI services to enhance marketing efforts through open-source intelligence (OSINT).

## Features
- **Multi-Tenancy**: Supports multiple tenants with strict data separation.
- **User Management**: Handles authentication, roles, and permissions.
- **AI Integration**: Centralized AI API for various AI clients (OpenAI, Gemini, Ollama).
- **Admin UI**: User-friendly interface for managing tenants and accessing AI services.
- **Backup Solutions**: Manual and AI-driven backup functionalities.

## Project Structure
```
osint_marketing_tool
├── app.py                  # Main entry point of the application
├── users.py                # User and role management
├── tenants.py              # Tenant management functionalities
├── manage_tenants.py       # Administrative tenant management
├── backup.py               # Manual backup functionality
├── backup_ai.py            # AI-driven backup processes
├── connectors               # External API integrations
│   └── __init__.py
├── utils                   # Utility functions and API clients
│   ├── openai_client.py
│   ├── gemini_client.py
│   ├── ollama_client.py
│   └── __init__.py
├── adminui                 # Admin UI components
│   ├── __init__.py
│   ├── ai_service.py       # AI service integration
│   ├── views.py            # Admin UI views and routes
│   └── templates
│       └── admin_ai.html   # Admin AI interface template
├── templates               # Base templates for the application
│   └── base.html
├── storage                 # Tenant-specific data storage
│   └── tenants
│       └── <tenant>/
├── .env                    # Environment variables
├── config.example.env      # Example configuration file
└── README.md               # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/puchadave/osint_marketing_tool.git
   cd osint_marketing_tool
   ```

2. Copy the example environment configuration:
   ```
   cp config.example.env .env
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To start the application, run:
```
python app.py
```
Access the admin UI at `http://localhost:5000/admin`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.