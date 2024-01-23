import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
# from scode.util import *

# ===============================================================================
#                               Definitions
# ===============================================================================

def fwrite(path: str, text, encoding='cp949'):
	text = str(text)
	
	if not text:
		text += '\n'
	elif text[-1] != '\n':
		text += '\n'
	
	try:
		with open(path, 'a', encoding=encoding) as f:
			f.write(text)
	except UnicodeEncodeError:
		try:
			with open(path, 'a', encoding='cp949') as f:
				f.write(text)
		except UnicodeEncodeError:
			with open(path, 'a', encoding='utf-8') as f:
				f.write(text)


def run():
	input_file_path = 'input.txt'
	output_file_path = 'output.txt'
	error_file_path = 'error.txt'
	
	open(output_file_path, 'w').close()

	# try:
	# 	input_lst = [x.strip() for x in open(input_file_path).read().splitlines()]
	# except UnicodeDecodeError:
	# 	input_lst = [x.strip() for x in open(input_file_path, encoding='UTF-8').read().splitlines()]
	
	# total_cnt = len(input_lst)

	driver_path = 'C:\chromedriver\chromedriver.exe'
	driver = webdriver.Chrome(executable_path=driver_path)
	driver.implicitly_wait(10)
	driver.set_window_size(450, 900)

	# 로그인 페이지 URL
	login_url = 'https://nid.naver.com/'

	# 웹 페이지 열기
	driver.get(login_url)

	# 로그인 정보
	username = ''
	password = ''

	# 아이디 입력 필드 찾기 및 클립보드를 통해 아이디 입력
	username_field = driver.find_element(By.ID, 'id')
	pyperclip.copy(username)
	username_field.click()
	ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

	# 잠시 대기
	time.sleep(1)

	# 비밀번호 입력 필드 찾기 및 클립보드를 통해 비밀번호 입력
	password_field = driver.find_element(By.ID, 'pw')
	pyperclip.copy(password)
	password_field.click()
	ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

	# 로그인 버튼 클릭
	login_button = driver.find_element(By.ID, 'log.login')
	login_button.click()

	# driver.quit()

	print("끝.")

# ===============================================================================
#                            Program infomation
# ===============================================================================

__author__ = '선준우'
__registration_date__ = '240123'
__latest_update_date__ = '240123'
__version__ = 'v1.00'
__title__ = '네이버 지식인 프로그램'
__desc__ = '지식인 '
__changeLog__ = {
	'v1.00': ['Initial Release.']
}
version_lst = list(__changeLog__.keys())

full_version_log = '\n'
short_version_log = '\n'

for ver in __changeLog__:
	full_version_log += f'{ver}\n' + '\n'.join(['    - ' + x for x in __changeLog__[ver]]) + '\n'

if len(version_lst) > 5:
	short_version_log += '.\n.\n.\n'
	short_version_log += f'{version_lst[-2]}\n' + '\n'.join(['    - ' + x for x in __changeLog__[version_lst[-2]]]) + '\n'
	short_version_log += f'{version_lst[-1]}\n' + '\n'.join(['    - ' + x for x in __changeLog__[version_lst[-1]]]) + '\n'

# ===============================================================================
#                                 Main Code
# ===============================================================================

if __name__ == '__main__':
	sys.stdout.write(f'{__title__} {__version__} ({__latest_update_date__})\n')
	sys.stdout.write(f'{short_version_log if short_version_log.strip() else full_version_log}\n')
	run()
