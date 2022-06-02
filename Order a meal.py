# Złóż zamówienie
# Order a meal
# Aplikacja pozwalająca wybrać pozycje z menu i oblicza ich cenę
# An app that lets you order food and calculate price

from tkinter import *

class Application(Frame):
    """
    Aplikacja z GUI
    """

    def __init__(self, master):
        """ inicjalizuj ramkę """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        Tworzę wszystkie potrzebne widżety
        """

        #Etykieta z tytułem
        Label(self,
              text = "MENU"
              ).grid(row = 0, column = 0, sticky = W)
        # Etykieta z instrukcją
        Label(self,
              text = "Wybierz swoje zamówienie i kliknij 'Akceptuj'"
              ).grid(row = 1, column = 0, columnspan = 2, sticky = W)
        #Pole wyboru z pozycjami
        self.is_schab = BooleanVar()
        Checkbutton(self,
                    text = "Schab z ziemniakami i surówką - 12 zł",
                    variable = self.is_schab
                    ).grid(row = 2, column = 0, sticky = W)
        self.is_kurczak = BooleanVar()
        Checkbutton(self,
                    text = "kurczak z ziemniakami i surówką - 12 zł",
                    variable = self.is_kurczak
                    ).grid(row = 3, column = 0, sticky = W)
        self.is_pstrag = BooleanVar()
        Checkbutton(self,
                    text = "Pstrąg z ziemniakami i surówką - 25 zł",
                    variable = self.is_pstrag
                    ).grid(row = 4, column = 0, sticky = W)
        self.is_tatar = BooleanVar()
        Checkbutton(self,
                    text = "Tatar wołowy z ogórkiem i chlebem - 20 zł",
                    variable = self.is_tatar
                    ).grid(row = 5, column = 0, sticky = W)

        # Tworzę przycisk akceptacji
        Button(self,
               text = "Akceptuj",
               command = self.show_message
               ).grid(row = 6, column = 0, sticky = W)
        self.menu_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.menu_txt.grid(row = 7, column = 0, columnspan = 3)

    def show_message(self):
        """ oblicz rachunek dla klienta """

        cena = 0
        if self.is_schab.get():
            cena += 12
        if self.is_kurczak.get():
            cena += 12
        if self.is_pstrag.get():
            cena += 25
        if self.is_tatar.get():
            cena += 20

        # tworzę komunikat o cenie

        menu = "Twój rachunek wynosi: ", cena," złotych"

        # wyświetlam komunikat

        self.menu_txt.delete(0.0, END)
        self.menu_txt.insert(0.0, menu)

#main
root = Tk()
root.title("Złóż zamówienie")
app = Application(root)
root.mainloop()
        
        














        
        
