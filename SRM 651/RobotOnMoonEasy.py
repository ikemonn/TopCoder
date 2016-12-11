# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class RobotOnMoonEasy:
    def isSafeCommand(self, board, S):
        x = 0
        y = 0
        max_y = len(board[0]) - 1
        max_x = len(board) - 1
        for row, col in enumerate(board):
            if col.find('S') > -1:
                x = row
                y = col.find('S')
                break

        for cmd in S:
            curr_x = x
            curr_y = y
            print "========== S ==========="
            print "curr_x", curr_x
            print "curr_y", curr_y

            if cmd == 'U':
                x -= 1
            elif cmd == 'D':
                x += 1
            elif cmd == 'R':
                y += 1
            elif cmd == 'L':
                y -= 1
            print "CMD", cmd
            print "x",x
            print "y",y


            if y < 0 or y > max_y or x < 0 or x > max_x:
                print "max_x", max_x
                print "max_y", max_y
                return 'Dead'
            else:
                # print "board", board[x][y]
                print "========== E ==========="

            if board[x][y] == '#':
                x = curr_x
                y = curr_y




        return 'Alive'

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(board, S, __expected):
    startTime = time.time()
    instance = RobotOnMoonEasy()
    exception = None
    try:
        __result = instance.isSafeCommand(board, S);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("RobotOnMoonEasy (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("RobotOnMoonEasy.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            board = []
            for i in range(0, int(f.readline())):
                board.append(f.readline().rstrip())
            board = tuple(board)
            S = f.readline().rstrip()
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(board, S, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1481358849
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
