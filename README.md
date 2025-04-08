MCA Sem 1 Project NestNavi is a web-based platform designed to simplify and streamline the rental process Developed as a part of the MCA Semester I mini-project at MES' IMCC, Pune, 
This system provides an interactive interface for both property owners and tenants.
Key Features 
User Roles: Owner: Can register, login, add property listings, update property status, and view tenant inquiries. Tenant: Can register, login, browse available properties, express interest, and book visits.
Dashboard Access: Owner dashboard displays listed properties and tenant inquiries. Tenant home page shows available PGs with options to inquire or book. Admin Panel: Admin can monitor user registrations and property listings. All backend activities are reflected through a SQLite-powered database.
Technology Stack: Frontend: HTML, CSS, JavaScript Backend: Django (Python) Database: SQLite
Database Tables Userauth_user – stores authentication details for owners and tenants. property_property – contains property listing information. home_tenantinquiry – manages tenant inquiries and visit bookings.
