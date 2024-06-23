import time

class NeTube:
    users = []
    videos = []
    some_users = None
    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.some_users = user

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f"Имя пользователя {nickname} занято")
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)

    def log_out(self):
        self.some_users = None

    def add(self, *args):
        for movie in args:
            self.videos.append(movie)

    def get_videos(self, world):
        list_video = []
        for i in self.videos:
            if world.lower() in i.title.lower():
                list_video.append(i.title)
        return list_video

    def watch_video(self, movie):
        if self.some_users and self.some_users.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.some_users:
            for roll in self.videos:
                if movie in roll.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


class Videos:
    def __init__(self, title, duration, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hash(self.password)


us = NeTube()
vid1 = Videos('Теории заговора с Игорем прокопенко', 200)
vid2 = Videos('Заменит ли ИИ программистов?', 10)

us.add(vid1, vid2)

us.watch_video('Заменит ли ИИ программистов?')
us.register('MadMax', 'MadMaxBlock99', 27)
us.watch_video('Заменит ли ИИ программистов?')
us.register('proga_HuNtEr', '290411IIp45s', 15)
us.watch_video('Заменит ли ИИ программистов?')

us.register('MadMax', '33rohjds', 62)
print(us.some_users)
us.watch_video('Заменит ли ИИ программистов?')