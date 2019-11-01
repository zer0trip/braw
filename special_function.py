import webbrowser
from urllib.request import urlretrieve
import os
import time


def print_function(text):
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode('ascii', errors='ignore').decode('ascii'))


def body_is_link(submission):
    url = submission.url
    if submission.over_18:
        print('Cautious: NSFW!!!!')
        allow_18 = input('Do you really wanna lose your job? y/n: ')
        if allow_18.lower() == 'y':
            print("You don't care. OK fine")
        else:
            print('I know, your job is more important')
            print("Won't show the link")
            return
    # For youtube
    if 'youtu.be' in url:
        print('There is a youtube video')
        ans = input('Do you want to watch now? y/n: ')
        if ans.lower() == 'y':
            print('No problem, will show in your browser after 5 seconds')
            print('Press Ctrl C to save your job.')
            for i in range(5, 0, -1):
                try:
                    print(i)
                    time.sleep(1)
                except KeyboardInterrupt:
                    print('Your job is safe')
                    return
            webbrowser.open_new_tab(url)
        elif ans.lower() == 'n':
            print('No problem.')
        else:
            print('Am I a joke to you?')
            print("I won't do anything.")
    # For image
    if any(img_suf in url for img_suf in ['jpg', 'png', 'gif']):
        print('There is an image')
        ans = input('Do you want to see now? y/n: ')
        if ans.lower() == 'y':
            print('No problem, will show in your browser after 5seconds')
            print('Press Ctrl C to save your job.')
            for i in range(5, 0, -1):
                try:
                    print(i)
                    time.sleep(1)
                except KeyboardInterrupt:
                    print('Your job is safe')
                    return
            webbrowser.open_new_tab(url)
        elif ans.lower() == 'n':
            print('No problem.')
            ans = input('Then do you want to save it? y/n: ')
            if ans.lower() == 'y':
                save_path = input('Where do you want to save the picture? :')
                if 'jpg' in url:
                    suffix = 'jpg'
                elif 'png' in url:
                    suffix = 'png'
                else:
                    suffix = 'gif'
                path = os.path.join(save_path, '{}.{}'.format(submission.id, suffix))
                urlretrieve(url, path)
                print('safe in {}'.format(path))
            elif ans.lower() == 'n':
                print('No problem.')
            else:
                print('Am I a joke to you?')
                print("I won't do anything.")
        else:
            print('Am I a joke to you?')
            print("I won't do anything.")
    else:
        print('There is a link')
        ans = input('Do you want to see now? y/n: ')
        if ans.lower() == 'y':
            print('No problem, will show in your browser after 5seconds')
            print('Press Ctrl C to save your job.')
            for i in range(5, 0, -1):
                try:
                    print(i)
                    time.sleep(1)
                except KeyboardInterrupt:
                    print('Your job is safe')
                    return
            webbrowser.open_new_tab(url)
        elif ans.lower() == 'n':
            print('No problem.')
        else:
            print('Am I a joke to you?')
            print("I won't do anything.")

    return

