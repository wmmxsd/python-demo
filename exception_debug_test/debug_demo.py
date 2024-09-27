def assert_demo(s):
    assert s != 0, 'n is zero'
    return 10 / s
# 启动Python解释器时可以用-O参数来关闭assert
assert_demo(3)
assert_demo(0)