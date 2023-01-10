import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
import json
import requests

class ui_consulta_ruc (QMainWindow):
    def __init__(self ):
        super().__init__()
        uic.loadUi("buscar-ruc.ui", self)
        self.btnBuscarRUC.clicked.connect(self.fn_buscarRuc)

    def fn_buscarRuc(self):
        rucBuscar = self.txtBuscarRuc.text()

        url = "https://www.softwarelion.xyz/api/sunat/consulta-ruc"
        token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozNDQ0LCJjb3JyZW8iOiJib3JhaGV5OTEyQHdlYm9ub2lkLmNvbSIsImlhdCI6MTY3MzMyMDE1OH0.c2L5L21Z3ebS_m44OisChde5z6d3l5CbVEroWnPMIHU"
        _json = { "ruc": rucBuscar }
        _headers = {'Content-Type': 'application/json', 'Authorization': token }

        response = requests.post(url, data= json.dumps(_json), headers=_headers)

        dataJson = response.json()

        if(dataJson['success'] == False):
            QMessageBox.warning(self, 'Juan', dataJson['message'])
            return
        empresa = dataJson['result']

        self.txtRazonSocial.setText(empresa['razonSocial'])    
        self.txtNombreComercial.setText(empresa['nombreComercial'])
        self.txtEstado.setText(empresa['estado'])
        self.txtCondicion.setText(empresa['condicion'])
        self.txtDireccion.setText(empresa['direccion'])
        self.txtDepartamento.setText(empresa['departamento'])
        self.txtProvincia.setText(empresa['provincia'])
        self.txtDistrito.setText(empresa['distrito'])
        self.txtTipoContribuyente.setText(empresa['tipoContribuyente'])
        self.txtFechaInscripcion.setText(empresa['fechaInscripcion'])
        self.txtFechaInicio.setText(empresa['fechaInicio'])
        self.txtActividadPrincipal.setText(empresa['actividadPrincipal'])

        actividades = ""

        for item in empresa['otrasActividades']:
            actividades += "*-"+item+"\n"

        self.txtActividadSecundaria.setText(actividades)
          
      #print(response.json())

       # print(rucBuscar)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ui_consulta_ruc()
    ui.show()
    sys.exit(app.exec_())        