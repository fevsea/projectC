from os import system as shell, environ, path

from projects.models import Project, BuildSteep



def populateDB():
    shell('mkdri -p media')
    if not path.isfile('media/projects/thumbnail/default.png'):
        shell('cp projects/static/img/default.png media/projects/thumbnail/default.png')

    for i in range(5):
        p = Project(title="Project title number {}".format(i),
                summary="Very short description. No much longer than a tweet",
                description="Lorem impsum dolor sit ammet. " * 5,
                details="Lorem impsum dolor sit ammet. " * 15,
                thumbnail="projects/thumbnail/default.png"
                )
        p.save()
        for j in range(3):
            BuildSteep(project=p,
                       content="Lorem impsum dolor sit ammet. " * 5,
                       number=j).save()


if __name__ == "__main__":
    # Generate secret file
    try:
        from projectC.secrets import *
    except ImportError:
        shell('cp projectC/secrets.py.template projectC/secrets.py')

    existDB = path.isfile('db.sqlite3')

    # DB creation
    shell('python3 manage.py makemigrations')
    shell('python3 manage.py migrate')

    if (not existDB):
        # Generic superuser
        # TODO: RELASE: delete email
        #shell('python3 manage.py createsuperuser --username admin --email alejandro.a.es@ieee.org')
        populateDB()


    # Tests
    shell('python3 manage.py test')
