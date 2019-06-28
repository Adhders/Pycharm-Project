class Node:
    def __init__(self, state_num, ch=None):
        self.state_num = state_num
        self.relation = {}
        self.ch = ch
        self.fail = None
        self.childvalue = [ ]
        self.children = [ ]


class Tree(Node):
    def __init__(self):
        super(Tree, self).__init__(0)  # 可以用Node.__init__(self,0) 调用非绑定方法
        self._state_num_max = 0
        self.g_dic = {}
        self.output_dic = {}

    def g(self, s, a):
        try:
            return self.g_dic[ (s, a) ]
        except:
            return 0

    def f(self, s):
        if s == 0:
            return 0

        return self.relation[ s ].fail.state_num

    def output(self, s):
        try:
            return self.output_dic[ s ]
        except:
            return [ ]

    def build(self, patterns):
        # 参数 pattern 如['he', 'she', 'his', 'hers']
        for pattern in patterns:
            self._build_from_pattern(pattern)
        self._build_fail()

    def _build_fail(self):
        queue = [ self ]
        while len(queue):
            temp = queue[ 0 ]
            queue.remove(temp)
            for i in temp.children:
                if temp == self:
                    i.fail = self
                else:
                    p = temp.fail
                    while p:
                        if i.ch in p.childvalue:
                            i.fail = p.children[ p.childvalue.index(i.ch) ]
                            break
                        p = p.fail
                    if not p:
                        i.fail = self
                queue.append(i)

    def _build_from_pattern(self, pattern):
        current = self
        for ch in pattern:
            # 判断是否存在
            index = self._ch_exist_in_node_children(current, ch)
            # 不存在 添加新节点并转向
            if index == -1:
                current = self._add_children_and_goto(current, ch)
            # 存在 直接goto
            else:
                current = current.children[ index ]
        # 输出函数
        self.output_dic[ current.state_num ] = [ pattern ]

    def _ch_exist_in_node_children(self, current, ch):
        """
        判断节点的孩子中是否存在 字符ch，如果存在返回位置；否则返回-1
        """
        for index in range(len(current.children)):
            child = current.children[ index ]
            if child.ch == ch:
                return index
        else:
            return -1

    def _add_children_and_goto(self, current, ch):
        """
        根据当前最大状态编号+1 和 字符ch，
        添加新节点并将新节点接入树中，并转向
        """
        # 状态编号加 1
        self._state_num_max += 1
        # 根据状态编号和ch 新建一个状态
        next_Node = Node(self._state_num_max, ch)
        # 将新建的状态添加为当前结点的子节点
        current.children.append(next_Node)
        # 修改转向函数
        self.g_dic[ (current.state_num, ch) ] = self._state_num_max
        self.relation[ self._state_num_max ] = next_Node

        # 返回将goto的节点
        current.childvalue.append(ch)
        return next_Node


class AC(Tree):
    def __init__(self):
        Tree.__init__(self)

    def init(self, patterns):
        # Tree.init(self)     当存在自定义初始化函数时，必须实现初始化
        Tree.build(self, patterns)

    def search(self, text):
        current_state = 0
        index = 0
        p = self
        patterns_appear_record = [ ]
        print("------search---------")
        while index < len(text):
            ch = text[ index ]
            next_state = self.g(current_state, ch)
            if next_state == 0:
                index -= 1
                # 字母未出现
                if current_state == 0:
                    index += 1
                else:
                    next_state = self.f(current_state)
            try:
                self.output_dic[ next_state ].extend(self.output(self.f(next_state)))
            except:
                self.output_dic[ next_state ] = self.output(self.f(next_state))

            print(str(current_state) + "," + ch, "->", next_state, self.output(next_state))
            if self.output(next_state) != [ ]:
                patterns_appear_record.append((index, self.output(next_state)))
            current_state = next_state
            index += 1

        print("\n出现过的模式及位置\n", patterns_appear_record)



if __name__ == "__main__":
    t = AC()
    t.init([ '幸福', 'this', 'ishe', 'hit', 'it', 'is' ])
    t.search("jshgsg幸福ssthishgs")