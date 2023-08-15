import json
from unittest.mock import patch, Mock
from airflow.models import DagBag, TaskInstance, XCom
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.utils.dates import days_ago
import pytest

class TestAPIDAG:

    @patch('airflow.providers.http.operators.http.HttpHook')
    def test_simple_http_operator(self, mock_http_hook):
        response_data = [
            {"id": 59250, "user_id": 4275659, "title": "Urbs stabilis tantillus carmen collum vinco.", "body": "Voro degenero allatus. Vigor tunc valens. Vel curvus sunt. Tumultus utrum rerum. Stips corroboro curso. Dicta patria alveus. Arceo alter ara. Tero avoco aestas. Ceno curriculum aureus. Vito vigilo adultus. Tendo calculus copia. Comburo comptus timidus. Pauper cilicium cariosus. Tutamen corrigo virgo."},
            # Add more response data items as needed
        ]

        mock_hook_instance = mock_http_hook.return_value
        mock_hook_instance.run.return_value = Mock(text=json.dumps(response_data))

        with patch.object(XCom, 'set', autospec=True) as mock_set_xcom:
            operator = SimpleHttpOperator(
                task_id='get_posts',
                http_conn_id='api_posts',
                endpoint='posts/',
                method='GET',
                response_filter=lambda response: json.loads(response.text),
                log_response=True
            )
            ti = TaskInstance(task=operator, execution_date=days_ago(1))
            operator.execute(context=ti.get_template_context())  # Simulate execution

            # Assert that the XCom data matches the expected response data
            mock_set_xcom.assert_called_once_with(
                key='return_value', value=json.dumps(response_data), task_ids='get_posts'
            )
