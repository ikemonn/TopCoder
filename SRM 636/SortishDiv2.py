# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class SortishDiv2:
    def ways(self, sortedness, seq):
        print "sortedness", sortedness
        print "seq", seq
        # 存在しない数字を見つける
        miss = []
        for x in range(1, len(seq)+1):
            if x not in seq:
                miss.append(x)
        print "miss:" + str(miss)
        ret = 0
        for perm in itertools.permutations(miss, len(miss)):
            print "======= perm ======="
            print perm
            # 全通りの数列を１つずつ試していく
            seq_ = list(seq)
            for p in perm:
                for i, s in enumerate(seq_):
                    if s == 0:
                        seq_[i] = p
                        break
            print "---------- seq_ -----------"
            print seq_

            so = 0
            for i in range(len(seq_)-1):
                for j in range(i+1, len(seq_)):
                    if seq_[i] < seq_[j]:
                        so += 1
            if so == sortedness:
                ret += 1
        return ret

                    # print "i:" + str(i)
                    # print "s:" + str(s)

        return 0

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

def do_test(sortedness, seq, __expected):
    startTime = time.time()
    instance = SortishDiv2()
    exception = None
    try:
        __result = instance.ways(sortedness, seq);
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
    sys.stdout.write("SortishDiv2 (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SortishDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            sortedness = int(f.readline().rstrip())
            seq = []
            for i in range(0, int(f.readline())):
                seq.append(int(f.readline().rstrip()))
            seq = tuple(seq)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(sortedness, seq, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1479634220
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
