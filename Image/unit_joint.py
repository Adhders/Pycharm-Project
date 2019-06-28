
def partion(vec,labels,predicate):
    N=len(vec)
    PARENT=0
    RANK=1
    nodes=[[0,0] for i in range(N)]
    for i in range(N):
        nodes[i][PARENT]=-1
        nodes[i][RANK]=0
    for i in range(N):
        root=i
        while(nodes[root][PARENT]>=0):
            root=nodes[root][PARENT];
        for j in range(i,N):
            if not predicate(vec[i],vec[j]):
                continue

            root2=j
            while(nodes[root2][PARENT]>=0):
                root2=nodes[root2][PARENT]
            #按照规模的大小合并树，将规模小的树合并到规模大的树上
            if(not root ==root2):
                rank=nodes[root][RANK]
                rank2=nodes[root2][RANK]
                if(rank>rank2):
                    nodes[root2][PARENT]=root
                else:
                    nodes[root][PARENT]=root2
                    nodes[root2][RANK]+=rank==rank2
                    root=root2
                assert(nodes[root][PARENT]<0)


                #以下分别对合并的两支进行路径压缩,缩短找root查询时间
                k=j
                while ((nodes[k][PARENT])>=0):
                    parent=nodes[k][PARENT]
                    nodes[k][PARENT]=root
                    k=parent

                k=i
                while ((nodes[k][PARENT])>=0):
                    parent=nodes[k][PARENT]
                    nodes[k][PARENT]=root
                    k=parent

    nclasses=0
    for i in range(N):
        root =i
        while(nodes[root][PARENT]>=0):
            root=nodes[root][PARENT]
        if (nodes[root][RANK]>=0):
            nclasses +=1
            nodes[root][RANK]=~nclasses#标记已经进行分类的分支为负值
        labels[i]=~nodes[root][RANK]

    return labels ,nclasses









if __name__=="__main__":
    vector=[2,3,8,15,9,16,5]
    labels=[0]*len(vector)
    labels=partion(vector,labels,lambda x,y:abs(x-y)<=2)
    print(labels)











