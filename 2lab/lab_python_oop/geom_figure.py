from  abc import ABCMeta, abstractmethod, abstractproperty


class Figure(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass
