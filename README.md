FurEver Home
============

A pet adoption platform built using Django Rest Framework (DRF), React, and Tailwind CSS. This platform features role-based access for adopters, shelters, and admins, allowing users to browse and apply for adoptions and join a pet community. It also includes tiered memberships (Basic, Moderate, Premium) to enhance the user experience with varying access to pet listings and community features.

Project Links:
--------------
- Preview: https://fur-ever-home.vercel.app/
- Client-Side Code: https://github.com/Rocky3698/FurEver_Home
- Server-Side Code: https://github.com/Rocky3698/FurEver_Home_API

Key Features:
-------------
- **Role-Based Access:** Different user roles (adopters, shelters, admins) with specific permissions and features.
- **Tiered Memberships:** Various levels of membership (Basic, Moderate, Premium) that provide different access to pet listings and community features.
- **Community Features:** Users can engage with the pet community through discussions, posts, and comments.

Technologies Used:
------------------
- **Backend:** Django Rest Framework (DRF)
- **Frontend:** React, Tailwind CSS
- **Database:** PostgreSQL

Setup Instructions:
-------------------
1. **Clone the repositories:**
   - `git clone https://github.com/Rocky3698/FurEver_Home`
   - `git clone https://github.com/Rocky3698/FurEver_Home_API`

2. **Backend Setup:**
   - Navigate to the `FurEver_Home_API` directory.
   - Create a virtual environment: `python -m venv env`
   - Activate the virtual environment:
     - On Windows: `env\Scripts\activate`
     - On MacOS/Linux: `source env/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
   - Apply migrations: `python manage.py migrate`
   - Start the server: `python manage.py runserver`

3. **Frontend Setup:**
   - Navigate to the `FurEver_Home` directory.
   - Install dependencies: `npm install`
   - Start the development server: `npm start`

4. **Access the application:**
   - Open your browser and navigate to `http://localhost:3000` for the frontend.
   - The backend API will be running on `http://localhost:8000`.

Contributing:
-------------
We welcome contributions to FurEver Home! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push the branch to your forked repository.
5. Open a pull request to the main repository.

Contact:
--------
For any questions or issues, please reach out to Rocky Chowdhury at [rocky20809@gmail.com](mailto:rocky20809@gmail.com).

License:
--------
This project is licensed under the MIT License. See the LICENSE file for more details.

