class Person:
    """Class that represents simple person which has no capabilities to work for the company"""
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'
    
class Worker(Person):
    def __repr__(self) -> str:
        return super().__init__()
    
    def do_the_job(self):
        print("I'm doing the job because I'm the worker")
    


class Company:
    """Actual company that contains the bunch of workers"""
    worker_list = []
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'
    
    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.worker_list.append(worker)
        else:
            raise ValueError(f'Invalid worker type. Only "Worker" applicable')
        
    
    def start(self):
        print('The company is going to begin its own internal job processes')

        for i in range(len(self.worker_list)):
            print(f'\t {i}th worker init')
            self.worker_list[i].do_the_job()


person = Person()
worker1 = Worker()
worker2 = Worker()
company = Company()

# company.add_worker(person) # this will fail
company.add_worker(worker1)
company.add_worker(worker2)
company.start()


