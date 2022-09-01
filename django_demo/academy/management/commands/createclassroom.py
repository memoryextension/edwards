from django.core.management.base import BaseCommand, CommandError
from academy.models import Classroom
from academy.utils import get_random_word

class Command(BaseCommand):
    help = 'Creates new classrooms'

    def add_arguments(self, parser):
        parser.add_argument('classrooms', type=int, help="Number of classrooms to be created.")

    def handle(self, *args, **options):
        classrooms = options['classrooms']
        for i in range(classrooms + 1):
            classroom = Classroom(name =  get_random_word())
            try:
                classroom.save()
            except Exception as e:
                self.stdout.write(self.style.ERROR("The classroom %s cannot be saved." % classroom.name))

        self.stdout.write(self.style.SUCCESS('Classrooms were created successfully.'))