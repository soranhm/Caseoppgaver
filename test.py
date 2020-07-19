from tkinter import *

class MyWindow:
    def __init__(self, win):
        # Setter opp vinduet
        self.ok =False
        self.befok = False
        self.leveok  =  False
        self.dodeok =  False
        self.innflok =  False
        self.utflyok =  False
        f_in = open('test.csv')
        self.fields = []
        for line in f_in.readlines():
            self.fields.append([item.strip('\n') for item in line.split(';')])

        self.ovsk = Label(win, text='Hele landet/Norge', font='Helvetica 14 bold')
        self.ovsk2 = Label(win, text='1951 - 2020', font='Helvetica 14 bold')
        self.info = Label(win, text='Søk etter år og oppdatere verdiene med \nknappen "Oppdater verdier"', font='Helvetica 14 bold')

        self.aar = Label(win, text='År :', font='Helvetica 14 bold')
        self.aarbox = Entry(bd=3,  font='Helvetica 16 bold' , width=4)

        self.innb = Label(win, text='Befolkning :', font='Helvetica 14 bold')
        self.innbbox = Entry(bd=3,  font='Helvetica 16 bold' , width=10)

        self.do = Label(win, text='Levendefødte :', font='Helvetica 14 bold')
        self.dobox = Entry(bd=3,  font='Helvetica 16 bold' , width=10)

        self.dode = Label(win, text='Døde :', font='Helvetica 14 bold')
        self.dodebox = Entry(bd=3,  font='Helvetica 16 bold', width=10)

        self.innfl = Label(win, text='Innflyttinger :', font='Helvetica 14 bold')
        self.innflbox = Entry(bd=3,  font='Helvetica 16 bold', width=10)

        self.utfl = Label(win, text='Utflyttinger :', font='Helvetica 14 bold')
        self.utflbox = Entry(bd=3,  font='Helvetica 16 bold', width=10)

        self.sokBtn = Button(win, text='SØK', command=lambda:  self.fin_(win), height=1, width=3, font='Helvetica 16 bold')
        self.lagreBtn = Button(win, text='Oppdater verdier', command=lambda:  self.change_(win), height=1, width=15, font='Helvetica 16 bold')
        #"region";"år";"statistikkvariabel";"06913: Befolkning og endringer, etter region, år og statistikkvariabel"

        self.ovsk.place(x=220, y=10)
        self.ovsk2.place(x=245, y=35)

        self.aar.place(x=10, y=100)
        self.aarbox.place(x=160, y=100)
        self.info.place(x=10, y=150)

        self.sokBtn.place(x=220, y=95)
        self.lagreBtn.place(x=120, y=460)

        self.innb.place(x=10, y=260)
        self.innbbox.place(x=160, y=260)

        self.do.place(x=10, y=300)
        self.dobox.place(x=160, y=300)

        self.dode.place(x=10, y=340)
        self.dodebox.place(x=160, y=340)

        self.innfl.place(x=10, y=380)
        self.innflbox.place(x=160, y=380)

        self.utfl.place(x=10, y=420)
        self.utflbox.place(x=160, y=420)
    def change_(self,win):
        # Endrer veridene i .csv fil
        f_out = open('test.csv', 'w')
        vals = '"{}"'.format(self.aarbox.get())
        for i in range(len(self.fields)):
            if self.fields[i][1] == vals:
                if self.fields[i][2] == '"{}"'.format("Befolkning"):
                    if self.innbbox.get() != self.fields[i][3]:
                        if self.innbbox.get():
                            self.fields[i][3] = self.innbbox.get()
                            self.innbbox.delete(0, 'end')

                elif self.fields[i][2] == '"{}"'.format("LevendefÃ¸dte"):
                    if self.dobox.get() != self.fields[i][3]:
                        if self.dobox.get():
                            self.fields[i][3] = self.dobox.get()
                            self.dobox.delete(0, 'end')

                elif self.fields[i][2] == '"{}"'.format("DÃ¸de"):
                    if self.dodebox.get() != self.fields[i][3]:
                        if self.dodebox.get():
                            self.fields[i][3] = self.dodebox.get()
                            self.dodebox.delete(0, 'end')

                elif self.fields[i][2] == '"{}"'.format("Innflyttinger"):
                    if self.innflbox.get() != self.fields[i][3]:
                        if self.innflbox.get():
                            self.fields[i][3] = self.innflbox.get()
                            self.innflbox.delete(0, 'end')

                elif self.fields[i][2] == '"{}"'.format("Utflyttinger"):
                    if self.utflbox.get() != self.fields[i][3]:
                        if self.utflbox.get():
                            self.fields[i][3] = self.utflbox.get()
                            self.utflbox.delete(0, 'end')

        for i in range(len(self.fields)):
            f_out.write(self.fields[i][0] + ';' + self.fields[i][1] + ';' + self.fields[i][2] + ';' + self.fields[i][3] +'\n')
        f_out.close()
        self.fin_(win)



    def fin_(self,win):
        # Finner verdiene til statistikkvariabelene
        vals = '"{}"'.format(self.aarbox.get())
        if self.befok:
            self.bef_org.destroy()
        if self.leveok:
            self.leve_org.destroy()
        if self.dodeok:
            self.dode_org.destroy()
        if self.innflok:
            self.innfl_org.destroy()
        if self.utflyok:
            self.utflyt_org.destroy()
        self.org = Label(win, text="Registrerte verdier",  bd=3, font='Helvetica 16 bold')
        self.org.place(x=320, y=220)
        for i in range(len(self.fields)):
            if self.fields[i][1] == vals:
                if self.fields[i][2] == '"{}"'.format("Befolkning"):
                    self.befok = True
                    self.bef_org = Label(win, text=self.fields[i][3],  bd=3, font='Helvetica 16 bold')
                    self.bef_org.place(x=320, y=260)
                elif self.fields[i][2] == '"{}"'.format("LevendefÃ¸dte"):
                    self.leveok = True
                    self.leve_org = Label(win, text=self.fields[i][3],  bd=3, font='Helvetica 16 bold')
                    self.leve_org.place(x=320, y=300)
                elif self.fields[i][2] == '"{}"'.format("DÃ¸de"):
                    self.dodeok = True
                    self.dode_org = Label(win, text=self.fields[i][3],  bd=3, font='Helvetica 16 bold')
                    self.dode_org.place(x=320, y=340)
                elif self.fields[i][2] == '"{}"'.format("Innflyttinger"):
                    self.innflok = True
                    self.innfl_org = Label(win, text=self.fields[i][3], bd=3, font='Helvetica 16 bold')
                    self.innfl_org.place(x=320, y=380)
                elif self.fields[i][2] == '"{}"'.format("Utflyttinger"):
                    self.utflyok = True
                    self.utflyt_org = Label(win, text=self.fields[i][3], bd=3, font='Helvetica 16 bold')
                    self.utflyt_org.place(x=320, y=420)

window = Tk()
mywin = MyWindow(window)
window.title('Caseoppgave')
window.geometry("550x600")
window.mainloop()
