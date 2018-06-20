#!/usr/bin/env

from eval import Eval

evaluator = Eval()
print("Output 1: %s" % evaluator.parse('12*0.5'))
print("Output 2: %s" % evaluator.parse('(2+0)^(2+3)/2*3^34*76/(9+123)'))
print("Output 3: %s" % evaluator.parse('2*3^2'))