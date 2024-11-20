import time
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    Users = []
    current_user = None
    videos = []
    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if self.Users == []:
            self.Users.append(new_user)
            self.current_user = new_user
        else:
            for user in self.Users:
                if new_user.nickname == user.nickname:
                    print(f'Пользователь {nickname} уже существует')
                    break
            else:
                self.Users.append(new_user)
                self.current_user = new_user

    def log_in(self, nickname, password):
        for user in self.Users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                break
        else:
            print(f'Пользователь {nickname} не найден, пройдите регистрацию')

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for video in other:
            self.videos.append(video)

    def get_videos(self, arg):
        slovo = arg.lower()
        spisok_filmov = []
        for video in self.videos:
            if slovo in video.title.lower():
                spisok_filmov.append(video.title)
        else:
            return spisok_filmov

    def watch_video(self, arg):
        title = arg
        for video in self.videos:
            if title == video.title:
                if self.current_user == None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif self.current_user.age < 18 and video.adult_mode == True:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(video.duration):
                        print(video.time_now +1, end=' ')
                        time.sleep(1)
                        video.time_now += 1
                    else:
                        print('Конец видео')
                        video.time_now = 0


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

ur.watch_video('Лучший язык программирования 2024 года!')