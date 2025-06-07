import ctypes
from ctypes import wintypes

#⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ALERTA DE CHATGPT ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️

# === AVISO DO DESENVOLVEDOR === 
# Prezado professor Henrique,
# Com o intuito de aprimorar a experiência visual do jogo, solicitei ao ChatGPT duas funções auxiliares:
# uma para aumentar o tamanho da fonte no CMD e outra para maximizar a janela do console, evitando que 
# caracteres fiquem cortados durante a execução.
#
# Este trecho de código deve ser entendido como um recurso estético complementar — uma licença poética.
# Ele não é essencial para o funcionamento do jogo e pode ser ignorado em termos de lógica principal.


# ===== Constantes e estruturas necessárias =====
STD_OUTPUT_HANDLE = -11
LF_FACESIZE       = 32
SW_SHOWMAXIMIZED  = 3

class COORD(ctypes.Structure):
    _fields_ = [("X", wintypes.SHORT), ("Y", wintypes.SHORT)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [
        ("cbSize",     wintypes.ULONG),
        ("nFont",      wintypes.DWORD),
        ("dwFontSize", COORD),
        ("FontFamily", wintypes.UINT),
        ("FontWeight", wintypes.UINT),
        ("FaceName",   wintypes.WCHAR * LF_FACESIZE)
    ]

# ===== Função para maximizar o console =====
def maximizar_console():
    GetConsoleWindow = ctypes.windll.kernel32.GetConsoleWindow
    ShowWindow       = ctypes.windll.user32.ShowWindow

    hwnd = GetConsoleWindow()
    if hwnd:
        ShowWindow(hwnd, SW_SHOWMAXIMIZED)

# ===== Função para ajustar a fonte para 50×50 =====
def letras_grande():
    h = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    f = CONSOLE_FONT_INFOEX()
    f.cbSize = ctypes.sizeof(f)

    # Carrega configurações atuais
    ctypes.windll.kernel32.GetCurrentConsoleFontEx(h, False, ctypes.byref(f))

    # Define nome da fonte (já presente no Windows) e tamanho 50×50
    f.FaceName     = "Lucida Console"
    f.dwFontSize.X = 32
    f.dwFontSize.Y = 32

    return bool(ctypes.windll.kernel32.SetCurrentConsoleFontEx(h, False, ctypes.byref(f)))

