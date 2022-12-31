from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import app, db


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())


# 設定 python manage.py shell 為啟動互動式指令 shell 的指令
@manager.shell
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()