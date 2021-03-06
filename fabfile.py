from fabric.api import env, run, cd, sudo, local, get


env.hosts = ['whereisyourpeep.com', ]
deploy_dir = '/srv/wsgi/wiyp/'


def virtualenv_run(cmd):
    run('workon wiyp && ' + cmd)


def virtualenv_local(cmd):
    local('workon wiyp && ' + cmd)


def deploy():
    git_pull()
    install_requirements()
    sync_db()
    reload_code()


def install():
    make_deploy_dir()
    git_clone()
    make_virtualenv()
    install_requirements()
    start_gunicorn()
    install_nginx_conf()
    enable_nginx_conf()
    reload_nginx_conf()
    create_db()
    sync_db()


def full_restart_gunicorn():
    stop_gunicorn()
    start_gunicorn()


def make_deploy_dir():
    sudo('mkdir ' + deploy_dir)
    sudo('chown wraithan:users ' + deploy_dir)


def git_clone():
    with cd('/srv/wsgi/'):
        run('git clone git@github.com:wraithan/wiyp.git')


def git_pull():
    with cd(deploy_dir):
        run('git pull')


def make_virtualenv():
    run('mkvirtualenv --no-site-packages wiyp')


def install_requirements():
    with cd(deploy_dir):
        virtualenv_run('pip install -r deploy_requirements.txt')


def start_gunicorn():
    with cd(deploy_dir):
        virtualenv_run('gunicorn_django --pid=' + deploy_dir +
                       '/gunicorn.pid --workers=2 -b 127.0.0.1:8003 --daemon deploy_settings.py')

def stop_gunicorn():
    with cd(deploy_dir):
        sudo('kill `cat gunicorn.pid`')


def install_nginx_conf():
    sudo('cp ' + deploy_dir +
         '/conf/wiyp.conf /etc/nginx/sites-available/wiyp.conf')


def enable_nginx_conf():
    sudo('ln -s /etc/nginx/sites-available/wiyp.conf'
         ' /etc/nginx/sites-enabled/wiyp.conf')


def reload_nginx_conf():
    sudo('/etc/rc.d/nginx check')
    sudo('/etc/rc.d/nginx reload')


def create_db():
    run('createdb wiyp')


def sync_db():
    with cd(deploy_dir):
        virtualenv_run('./manage.py migrate')


def reload_code():
    with cd(deploy_dir):
        sudo('kill -HUP `cat gunicorn.pid`')

