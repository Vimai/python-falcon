import os
import json
import falcon
import logging
import requests

from datetime import datetime
from decimal import Decimal
from requests.exceptions import HTTPError


class Report:
    def __init__(self):
        self.logger = logging.getLogger('thingsapp.' + __name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(name)s - %(message)s')

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def on_get(self, req, res):
        self.logger.info(f'Start: GET')
        res.status = falcon.get_http_status(status_code=200)
        try:
            # response = requests.get('http://www.mocky.io/v2/5ea8c3162d0000644f3a40f0')
            response = []
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Other error occurred: {err}')

        # response_dict = response.json()

        scr_call = self._mock()
        total = 0
        relatorio = {}
        relatorio_full = {}

        for operation_item in scr_call.get('operation_items'):
            total += operation_item.get('due_value')
            if operation_item.get('due_type').get('due_code'):
                due_code = str(operation_item['due_type']['due_code'])
                if not relatorio.get(due_code):
                    relatorio[due_code] = operation_item.get('due_value')
                else:
                    relatorio[due_code] += operation_item.get('due_value')

            due_code = str(operation_item['due_type']['due_code'])
            category_code = str(operation_item['category_sub']['category']['category_code'])
            category_sub_code = str(operation_item['category_sub']['category_sub_code'])

            index = f'{category_code}_{category_sub_code}_{due_code}'
            if not relatorio.get(index):
                relatorio_full[index] = operation_item.get('due_value')
            else:
                relatorio_full[index] += operation_item.get('due_value')

        res.body = json.dumps(relatorio_full)
        self.logger.info(f'End.')

    @staticmethod
    def _mock():
        return {
                    "assumed_coobligation": 0.0,
                    "disagreement_operation_count": 0,
                    "disagreement_operation_value": 0.0,
                    "financial_institution_count": 12,
                    "indirect_risk": 0.0,
                    "operation_count": 337,
                    "operation_items": [
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "13",
                                "description": "cheque especial"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 91 a 180 dias",
                                "due_code": 140,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 42349.05,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "13",
                                "description": "cheque especial"
                            },
                            "due_type": {
                                "description": "Créditos a vencer até 30 dias",
                                "due_code": 110,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 503864.59,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 19,
                                    "category_description": "Limite"
                                },
                                "category_sub_code": "1",
                                "description": "contratado e não utilizado"
                            },
                            "due_type": {
                                "description": "Limite de crédito com vencimento até 360 dias",
                                "due_code": 20,
                                "due_type_group": "Limite de Credito"
                            },
                            "due_value": 3820370.88,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 4,
                                    "category_description": "Financiamentos"
                                },
                                "category_sub_code": "1",
                                "description": "aquisição de bens – veículos automotores"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 91 a 180 dias",
                                "due_code": 140,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 14324.44,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 4,
                                    "category_description": "Financiamentos"
                                },
                                "category_sub_code": "1",
                                "description": "aquisição de bens – veículos automotores"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 181 a 360 dias",
                                "due_code": 150,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 27285.95,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 4,
                                    "category_description": "Financiamentos"
                                },
                                "category_sub_code": "1",
                                "description": "aquisição de bens – veículos automotores"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 361 a 720 dias",
                                "due_code": 160,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 49555.44,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 4,
                                    "category_description": "Financiamentos"
                                },
                                "category_sub_code": "1",
                                "description": "aquisição de bens – veículos automotores"
                            },
                            "due_type": {
                                "description": "Créditos a vencer até 30 dias",
                                "due_code": 110,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 4983.36,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 4,
                                    "category_description": "Financiamentos"
                                },
                                "category_sub_code": "1",
                                "description": "aquisição de bens – veículos automotores"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 31 a 60 dias",
                                "due_code": 120,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 4932.37,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 4,
                                    "category_description": "Financiamentos"
                                },
                                "category_sub_code": "1",
                                "description": "aquisição de bens – veículos automotores"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 61 a 90 dias",
                                "due_code": 130,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 4878.45,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 4,
                                    "category_description": "Financiamentos"
                                },
                                "category_sub_code": "1",
                                "description": "aquisição de bens – veículos automotores"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 721 a 1080 dias",
                                "due_code": 165,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 33179.0,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 61 a 90 dias",
                                "due_code": 130,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 183564.64,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 1801 a 5400 dias",
                                "due_code": 180,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 21452.19,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 181 a 360 dias",
                                "due_code": 150,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 1017852.06,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 31 a 60 dias",
                                "due_code": 120,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 185743.89,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 1441 a 1800 dias",
                                "due_code": 175,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 648616.1,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 1081 a 1440 dias",
                                "due_code": 170,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 714251.36,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 91 a 180 dias",
                                "due_code": 140,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 524088.43,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer até 30 dias",
                                "due_code": 110,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 191695.38,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 721 a 1080 dias",
                                "due_code": 165,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 858087.25,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 12,
                                    "category_description": "Operações de arrendamento"
                                },
                                "category_sub_code": "1",
                                "description": "arrendamento financeiro exceto veículos automotores e imóveis"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 361 a 720 dias",
                                "due_code": 160,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 1657646.29,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "14",
                                "description": "conta garantida"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 361 a 720 dias",
                                "due_code": 160,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 5201.96,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "14",
                                "description": "conta garantida"
                            },
                            "due_type": {
                                "description": "Créditos a vencer até 30 dias",
                                "due_code": 110,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 3291106.45,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "14",
                                "description": "conta garantida"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 31 a 60 dias",
                                "due_code": 120,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 20147.17,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "16",
                                "description": "capital de giro com prazo vencimento superior 365 d"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 91 a 180 dias",
                                "due_code": 140,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 1180589.93,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "16",
                                "description": "capital de giro com prazo vencimento superior 365 d"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 181 a 360 dias",
                                "due_code": 150,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 1524626.48,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "16",
                                "description": "capital de giro com prazo vencimento superior 365 d"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 361 a 720 dias",
                                "due_code": 160,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 1071261.75,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "16",
                                "description": "capital de giro com prazo vencimento superior 365 d"
                            },
                            "due_type": {
                                "description": "Créditos a vencer até 30 dias",
                                "due_code": 110,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 330057.6,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "16",
                                "description": "capital de giro com prazo vencimento superior 365 d"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 31 a 60 dias",
                                "due_code": 120,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 393042.9,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "16",
                                "description": "capital de giro com prazo vencimento superior 365 d"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 61 a 90 dias",
                                "due_code": 130,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 392217.06,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "16",
                                "description": "capital de giro com prazo vencimento superior 365 d"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 721 a 1080 dias",
                                "due_code": 165,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 284695.92,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "15",
                                "description": "capital de giro com prazo de vencimento até 365 d"
                            },
                            "due_type": {
                                "description": "Créditos a vencer até 30 dias",
                                "due_code": 110,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 8698.69,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 2,
                                    "category_description": "Empréstimos"
                                },
                                "category_sub_code": "15",
                                "description": "capital de giro com prazo de vencimento até 365 d"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 61 a 90 dias",
                                "due_code": 130,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 1000000.0,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 3,
                                    "category_description": "Títulos descontados Direitos creditórios descontados"
                                },
                                "category_sub_code": "1",
                                "description": "desconto de duplicatas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 91 a 180 dias",
                                "due_code": 140,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 128503.14,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 3,
                                    "category_description": "Títulos descontados Direitos creditórios descontados"
                                },
                                "category_sub_code": "1",
                                "description": "desconto de duplicatas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer até 30 dias",
                                "due_code": 110,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 2721259.67,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 3,
                                    "category_description": "Títulos descontados Direitos creditórios descontados"
                                },
                                "category_sub_code": "1",
                                "description": "desconto de duplicatas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 31 a 60 dias",
                                "due_code": 120,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 1720888.39,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 3,
                                    "category_description": "Títulos descontados Direitos creditórios descontados"
                                },
                                "category_sub_code": "1",
                                "description": "desconto de duplicatas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 61 a 90 dias",
                                "due_code": 130,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 1079720.79,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 15,
                                    "category_description": "Coobrigações"
                                },
                                "category_sub_code": "2",
                                "description": "beneficiários de garantias prestadas para operações com outras pessoas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 91 a 180 dias",
                                "due_code": 140,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 738328.3,
                            "exchange_variation": "S"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 15,
                                    "category_description": "Coobrigações"
                                },
                                "category_sub_code": "2",
                                "description": "beneficiários de garantias prestadas para operações com outras pessoas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 181 a 360 dias",
                                "due_code": 150,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 1476656.6,
                            "exchange_variation": "S"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 15,
                                    "category_description": "Coobrigações"
                                },
                                "category_sub_code": "2",
                                "description": "beneficiários de garantias prestadas para operações com outras pessoas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 361 a 720 dias",
                                "due_code": 160,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 2490849.22,
                            "exchange_variation": "S"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 15,
                                    "category_description": "Coobrigações"
                                },
                                "category_sub_code": "2",
                                "description": "beneficiários de garantias prestadas para operações com outras pessoas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 31 a 60 dias",
                                "due_code": 120,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 462464.15,
                            "exchange_variation": "S"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 15,
                                    "category_description": "Coobrigações"
                                },
                                "category_sub_code": "2",
                                "description": "beneficiários de garantias prestadas para operações com outras pessoas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 61 a 90 dias",
                                "due_code": 130,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 275864.15,
                            "exchange_variation": "S"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 15,
                                    "category_description": "Coobrigações"
                                },
                                "category_sub_code": "2",
                                "description": "beneficiários de garantias prestadas para operações com outras pessoas"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 721 a 1080 dias",
                                "due_code": 165,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 275864.34,
                            "exchange_variation": "S"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 15,
                                    "category_description": "Coobrigações"
                                },
                                "category_sub_code": "1",
                                "description": "beneficiários de garantias prestadas para operações com PJ financeira"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 181 a 360 dias",
                                "due_code": 150,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 159623.63,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 15,
                                    "category_description": "Coobrigações"
                                },
                                "category_sub_code": "1",
                                "description": "beneficiários de garantias prestadas para operações com PJ financeira"
                            },
                            "due_type": {
                                "description": "Créditos a vencer de 721 a 1080 dias",
                                "due_code": 165,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 6333333.34,
                            "exchange_variation": "N"
                        },
                        {
                            "category_sub": {
                                "category": {
                                    "category_code": 1,
                                    "category_description": "Adiantamentos a depositantes"
                                },
                                "category_sub_code": "1",
                                "description": "adiantamentos a depositantes"
                            },
                            "due_type": {
                                "description": "Créditos a vencer até 30 dias",
                                "due_code": 110,
                                "due_type_group": "A vencer"
                            },
                            "due_value": 13333.64,
                            "exchange_variation": "N"
                        }
                    ],
                    "receive_coobligation": 0.0,
                    "reference_date": "2020-01",
                    "start_relationship": "2004-04-01",
                    "subjudice_operations_count": 0,
                    "subjudice_operations_value": 0.0
                }
