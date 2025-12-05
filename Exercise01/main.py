from queue import Queue
import random
import time

class Request:
    def __init__(self, id):
        self.id = id

class Program:
    def __init__(self):
        self.requests = Queue()

    def generate_requests(self, request):
        self.requests.put(request)
    
    def process_request(self):
        if not self.requests.empty():
            while not self.requests.empty():
                current_request = self.requests.get()
                print(f'Request with id {current_request.id} was processed')
        else:
            print(f'The queue is empty')


def main():
    q = Program()

    try:
        while True:
            for i in range(random.randint(1, 100)):
                q.generate_requests(Request(f'{i}'))

            q.process_request()
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nProgram was finished by user")


if __name__ == "__main__":
    main()
