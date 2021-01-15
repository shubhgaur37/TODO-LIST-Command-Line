import sys
import os
from datetime import date

def help():
    print('''Usage:-
    $ python todo.py add "todo item"  # Add a new todo
    $ python todo.py ls               # Show remaining todos
    $ python todo.py del NUMBER       # Delete a todo
    $ python todo.py done NUMBER      # Complete a todo
    $ python todo.py help             # Show usage
    $ python todo.py report           # Statistics''')


def add(todo):
    if len(todo)==0:
        print('Error: Missing todo string. Nothing added!')
        return
    f=open('todo.txt','a')
    f.write(todo+'\n')
    f.close()
    print('Added todo: ',end='')
    print('"'+todo+'"')
    
    
def ls():
    try:
        f=open('todo.txt','r')
    except IOError:
        print('There are no pending todos!')
        return
    else:
        todos=f.readlines()
        if len(todos)==0:
            print('There are no pending todos!')
        for i in range(len(todos)-1,-1,-1):
            print('['+str(i+1)+'] '+todos[i],end='')
        f.close()

def delete(index):
    try:
        f=open('todo.txt','r')
    except IOError:
        print('Error: todo #'+str(index)+' does not exist. Nothing deleted.')
        return
    else:
    
        todos=f.readlines()
    
        f.close()
        if index>len(todos) or index<1:
            print('Error: todo #'+str(index)+' does not exist. Nothing deleted.')
        else:
            todos.pop(index-1)
            f=open('todo.txt','w')
            for i in todos:
                f.write(i)
            f.close()
            print('Deleted todo #'+str(index))
    
def done(index):
    try:
        f=open('todo.txt','r')
    except IOError:
        print('Error: todo #'+str(index)+' does not exist.')
        return
    else:
        todos=f.readlines()
        f.close()
        if index>len(todos) or index<1:
            print('Error: todo #'+str(index)+' does not exist.')
        else:
            element=todos.pop(index-1)
            f=open('todo.txt','w')
            for i in todos:
                f.write(i)
            f.close()
            today=date.today()
            f=open('done.txt','a+')
            f.write('x '+str(today)+' '+element)
            f.close()
            print('Marked todo #'+str(index)+' as done.')
        

def report():
    today=date.today()
    
    try:
        f1=open('todo.txt')
    except IOError:
        print('''No Todos Added.
        Add a todo first in order to generate a report''')
        return
    
    try:
        f2=open('done.txt')
    except IOError:
        pendingTodos=len(f1.readlines())
        print('Pending :',pendingTodos,'Completed :',0)
        return
    else:
        pendingTodos=len(f1.readlines())
    
    doneTodos=len(f2.readlines())
    print(str(today),end=' ')
    
    print('Pending :',pendingTodos,'Completed :',doneTodos)
    
def todo(a):
    if len(a)>1:
        choice=a[1]
    else:
        choice=''
    
    if choice=='' or choice=='help':
        help()
    elif choice=='add':
        str=''
        for i in range(2,len(a)):
            str+=a[i]+' '
        add(str[:len(str)-1])
    elif choice=='del':
        if len(a)<3:
            print('Error: Missing NUMBER for deleting todo.')
            return
        else:
            todoNumber=int(a[2])
            delete(todoNumber)
    elif choice=='ls':
        ls()
    elif choice=='done':
        if len(a)<3:
            print('Error: Missing NUMBER for marking todo as done.')
            return
        else:
            todoNumber=int(a[2])
            done(todoNumber)
    elif choice=='report':
        report() 


#MAIN 
todo(sys.argv)
    
