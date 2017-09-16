from HTMLTestRunner import HTMLTestRunner
import unittest,time

if __name__ == '__main__':
	now = time.strftime("%Y-%m-%d %H-%M-%S")
	filename = '../test/html/' + now + 'result.html'

	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')

	discover = unittest.defaultTestLoader.discover('../test/qx/tjbb',pattern='test_ys.py')
	runner.run(discover)
	fp.close()