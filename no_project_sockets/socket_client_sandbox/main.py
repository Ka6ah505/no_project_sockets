import sys

from PyQt5.QtWidgets import QApplication
from no_project_sockets.socket_client_sandbox.gui import ClientGUI


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = ClientGUI()
    sys.exit(app.exec_())
