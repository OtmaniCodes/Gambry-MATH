# imports:
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.dialog import MDDialog
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import (Screen, ScreenManager, FadeTransition,
                                    TransitionBase, NoTransition, WipeTransition)
from kivymd.toast import toast
import math

class Operations:
    def __init__(self, num1=0, num2=0, ope=''):
        self.num1= float(num1)
        self.num2= float(num2)
        self.ope= ope

    def make_operation(self):
        try:
            if self.ope == "+":
                self.res= self.num1 + self.num2
            elif self.ope == "-":
                self.res= self.num1 - self.num2
            elif self.ope == "x":
                self.res= self.num1 * self.num2
            elif self.ope == "/":
                try:
                    self.res= self.num1 / self.num2
                except ZeroDivisionError as ex:
                    app.errors("sorry! you can't devide by 0")
                    self.res= self.num1
            elif self.ope == "%":
                self.res= self.num1 % self.num2
            elif self.ope == "^":
                self.res= self.num1 ** self.num2
            return self.res
        except Exception as ex:
            app.errors('looks like you have a '+str(ex))


class Starting(Screen):
    pass
class Home(Screen):
    pass
class Normal(Screen):
    pass
class Advanced(Screen):
    pass
 

class MainApp(MDApp):
    operation_elements= []
    sett= 0
    r_or_d=[]
    def build(self):
        Window.size= 360, 619    
        return Builder.load_file('main.kv')

    def on_start(self):
        Clock.schedule_once(self.one, 1)
        Clock.schedule_once(self.two, 1)
        Clock.schedule_once(self.three, 1)
        Clock.schedule_once(self.change_to_home, 9)



    #Animation:
    def one(self, *args):
        widget1= self.root.ids.start.ids.slide_one
        an1= Animation(yy= 1, d= 1)
        an1.start(widget1)
        
    def two(self, *args):
        widget2= self.root.ids.start.ids.slide_two
        an1= Animation(yy= 0.5, d= 1)
        an1.start(widget2) 

    def three(self, *args):
        widget3= self.root.ids.start.ids.lbl00
        widget4= self.root.ids.start.ids.me
        an1= Animation(op= 1, d= 2)
        an1+= Animation(underline= True, d= 3.5)
        an2= Animation(o=1, d= 3)
        an1.start(widget3)
        an2.start(widget4) 

    #Switching screens:
    def change_to_home(self, *args):
        current_screen= self.root.ids.screen_manager
        current_screen.transition= FadeTransition()
        current_screen.current= 'home_page'

    def change_to_normal(self, *args):
        current_screen2= self.root.ids.screen_manager
        current_screen2.transition.direction= 'up'
        current_screen2.transition= WipeTransition()
        current_screen2.current= 'normal_calculator'

    def change_to_advanced(self, *args):
        current_screen3= self.root.ids.screen_manager
        current_screen3.transition= WipeTransition()
        current_screen3.current= 'advanced_calculator'  

    def go_to_home(self, txt):
        if txt=='b':
            self.change_to_home()
        else:
            self.change_to_home()
            txt.text= ''
    #changing bg and fg colors:
    def change_color(self, chosen_btn):
        
        if chosen_btn == 'normal':
            item= self.root.ids.home.ids.b1
        elif chosen_btn == 'advanced': 
            item= self.root.ids.home.ids.b2
        elif chosen_btn == 'history': 
            item= self.root.ids.home.ids.b3
        elif chosen_btn == 'about': 
            item= self.root.ids.home.ids.b4

        an= Animation(md_bg_color= [0,0,0,1], text_color= [1,1,1,1], d= 0.1)
        an+= Animation(md_bg_color= [1,1,1,1], text_color= [0,0,0,1], d= 0.1)
        an.start(item)
    #doing the logic:
    def operate(self, num1, ope):
        self.num1= num1
        self.ope= ope

    def get_res(self, num2, txt, w):
        self.num2= num2
        self.txt= txt
        self.operator= Operations(self.num1, self.num2, self.ope)
        self.res= str(self.operator.make_operation())
        txt.text= ''
        if self.res[self.res.find('.'):] == ".0":
            txt.text= self.res[:self.res.find('.')]
        else:
            txt.text= str(self.res)
    def make_it_n(self, textt, txt2):
        txt2.text= str(-int(textt))

    def powerten2(self, txt2, txt):
        txt2.text= str(int(txt)*(10**2))
    def powerten3(self, txt2, txt):
        txt2.text= str(int(txt)*(10**3))
    
    def make_ad_operation(self, txt2, the_txt, what):
        self.the_txt= float(the_txt)
        try:
            if what == 'abs':
                self.sett= abs(self.the_txt)
            elif what == 'log':
                self.sett= math.log(self.the_txt)
            elif what =='root':
                self.sett= math.sqrt(self.the_txt)
            elif what == 'po2':
                self.sett= self.the_txt**2
            elif what == 'p3':
                self.sett= self.the_txt**3
            elif what == "cos":
                self.sett= math.cos(self.the_txt)
            elif what == "sin":
                self.sett= math.sin(self.the_txt)
            elif what == "tan":
                self.sett= math.tan(self.the_txt)
            elif what == "exp":
                self.sett= math.exp(self.the_txt)
            txt2.text= str(self.sett)
        except Exception as ex:
            self.errors('looks like you have a '+str(ex))

    def d_r(self,txt2, txt, n):
        self.r_or_d.append(n)
        if sum(self.r_or_d)%2==0:
            txt2.text=str( math.radians(float(txt)))
        elif sum(self.r_or_d)%2!=0:
            txt2.text= str(math.degrees(float(txt)))

    def errors(self, what):
        self.what= str(what)
        err=MDDialog(size_hint=(None, None), size=(320,150), pos_hint={'center_x':.5, 'center_y':.5},
                    title='Error!', text=self.what.title(), auto_dismiss=False)
        err.open()

        
if __name__ == '__main__':
    app= MainApp()
    app.run()