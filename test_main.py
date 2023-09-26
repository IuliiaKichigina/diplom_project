# Юлия Кичигина, 8а когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request


# 4.Проверить, что код ответа равен 200.
def test_receive_info():
    info_response = sender_stand_request.get_info()
    assert info_response.status_code == 200