# coding: utf8
__version__ = '10'

from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.utils import platform

from jnius import autoclass
from gui import gui



SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
    packagename=u'org.kivy.oscservice',
    servicename=u'Pong'
)


class App(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

    def build(self):

        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, 
                    Permission.WRITE_EXTERNAL_STORAGE, 
                    Permission.INTERNET,
                    Permission.ACCESS_NETWORK_STATE])      

        self.service = None
        return Builder.load_string(gui)




    def start_service(self):
        if platform == 'android':
            service = autoclass(SERVICE_NAME)
            self.mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity
            argument = ''
            service.start(self.mActivity, argument)
            self.service = service


        elif platform in ('linux', 'linux2', 'macos', 'win'):
            from runpy import run_path
            from threading import Thread
            self.service = Thread(
                target=run_path,
                args=['src/service.py'],
                kwargs={'run_name': '__main__'},
                daemon=True
            )
            self.service.start()
        else:
            raise NotImplementedError(
                "service start not implemented on this platform"
            )

    def calc_nota(self, nota1, nota2, nota3):
    
        self.start_service()  # Iniciamos el servicio para crear el server

        msj = ''

        try:
            corte1 = int(self.root.ids.corte1.text) / 100
            corte2 = int(self.root.ids.corte2.text) / 100
            corte3 = int(self.root.ids.corte3.text) / 100
        except:
            msj = 'Error: '
            msj += 'Porcentajes de cortes. '

        try:
            nota1 = float(nota1)
            nota2 = float(nota2)
            nota3 = float(nota3)
        except:
            msj += 'Notas cortes.'

        if not msj:
            nota = (corte1 * nota1) + (corte2 * nota2) + (corte3 * nota3)
            msj = 'Tu nota final es: ' +  str(nota)
        
        self.root.ids.notafinal.text = msj



if __name__ == '__main__':
    App().run()