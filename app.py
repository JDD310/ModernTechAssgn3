from flask import Flask, flash, redirect, render_template, request, url_for

from password_manager import PasswordManagerStore


def create_app(testing=False):
    app = Flask(__name__)
    app.testing = testing
    app.secret_key = 'dev-secret-key-change-me' if not testing else 'test-secret-key'
    store = PasswordManagerStore()

    @app.route('/')
    def index():
        return render_template('index.html', entries=store.list_entries())

    @app.route('/entries', methods=['POST'])
    def add_entry():
        title = request.form.get('title', '').strip()
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not title or not username or not password:
            flash('All fields are required.', 'error')
            return redirect(url_for('index'))

        store.add_entry(title=title, username=username, password=password)
        flash('Password saved successfully.', 'success')
        return redirect(url_for('index'))

    @app.route('/entries/<int:entry_id>/delete', methods=['POST'])
    def delete_entry(entry_id):
        store.delete_entry(entry_id)
        flash('Entry deleted.', 'success')
        return redirect(url_for('index'))

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
