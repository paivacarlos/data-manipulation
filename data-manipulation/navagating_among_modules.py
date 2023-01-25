from first_level_paste import first_level_file as file_01
from first_level_paste.second_level_paste import second_level_file as file_02

teste_01 = file_01.class_first_level_main()
teste_01.print_first_level_msg('Omega')
teste_01.from_first_level_file_msg_from_second_file('Delta - inside first class level called second level msg')

teste_02 = file_02.class_second_level()
teste_02.print_sencod_level_msg('Beta')
