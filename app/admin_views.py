from app import app

@app.route('/admin/dashboard')
def admin_dashboard():
    return "ADMIN DASHBOARD!"

@app.route('/admin/profile')
def admin_profile():
    return "<h3>This is the Admin Profile page</h3>"
