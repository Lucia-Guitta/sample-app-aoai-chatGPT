import re

import datetime
import time

pattern = r'\[doc\d+\]'


def checkDocRef(text: str, non_domain_questions: int) -> int:
    """
    Find occurrences of '[docN]' in the given text.

    Args:
        text (str): The text to search for '[docN]' occurrences.
        non_domain_quetions (int): the current number of questions out of the index scope
    Returns:
        int: the number of questions out of the index scope updated
    """
    pattern = r'\[doc\d+\]'
    if not re.findall(pattern, text):
        return True
    else:
        return False


def fixResponse(answer: str) -> str:
    return answer


class DailyDict(dict):
    def __init__(self):
        super().__init__()
        self.last_reset_date = datetime.date.today()

    def reset_if_needed(self):
        today = datetime.date.today()
        if today > self.last_reset_date:
            self.clear()
            self.last_reset_date = today


if __name__ == "__main__":
    referenced_text = """
Prop360 es un sistema de gestión de información para corredores de propiedades desarrollado por Convecta. 
Proporciona herramientas para la trazabilidad, seguimiento y generación de informes en el negocio del Real Estate. 
El sistema permite el ingreso y almacenamiento de información en la nube, la gestión de propiedades y clientes, 
el análisis de reportes y métricas, y la administración de intereses de los clientes. Prop360 también incluye 
un sitio web fácil de usar para compartir información sobre las propiedades y publicarlas automáticamente en 
los portales inmobiliarios con los que el cliente tenga contrato comercial. El módulo funciona en dispositivos 
de escritorio y móviles, y se divide en secciones como el Dashboard de Inicio, Sistema, Clientes, Propiedades 
y Reportes. Prop360 tiene diferentes flujos de trabajo, como Monooﬁcina o Multioﬁcina, y puede tener o no un 
flujo de visación dependiendo de los permisos de los usuarios. [doc0][doc1][doc2]
"""
    not_referenced_text = "Hoy hace 17º"

    non_domain_questions = 0
    print("Non domain questions", non_domain_questions)
    non_domain_questions = findDocRef(
        not_referenced_text, non_domain_questions)
    print("Non domain questions after non referenced text", non_domain_questions)
    non_domain_questions = findDocRef(
        not_referenced_text, non_domain_questions)
    print("Non domain questions after 2 non referenced text", non_domain_questions)
    non_domain_questions = findDocRef(referenced_text, non_domain_questions)
    print("Non domain questions", non_domain_questions)
    non_domain_questions = findDocRef(
        not_referenced_text, non_domain_questions)
    print("Non domain questions after non referenced text", non_domain_questions)
