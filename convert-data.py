#encoding=utf-8
import json

#树的后根遍历
def traverse(node, func):
    if node and node['children']:
        for child in node['children']:
            traverse(child, func)
    func(node)

#清除节点的多余属性，树使用孩子表示法进行表示
def clearNode(node):
    if node:
        del node['parent']
        del node['depth']
        if not node['children']:
            del node['children']

root = {'code':'','name':'中国','children':[],'parent':None,'depth':None}
curNode = root
curDepth = 0
f = open('./xzqh.txt','r')
for line in f:
    code, name = line.split()
    depth = 1 if code.endswith('0000') else 2 if code.endswith('00') else 3
    node = {'code':code,'name':name,'children':[],'parent':None,'depth':depth}
    if depth > curDepth and curNode['code'][:curDepth*2] == code[:curDepth*2]:
        node['parent'] = curNode
        curNode['children'].append(node)
    else :
        while depth < curDepth and curNode['parent'] and \
            curNode['parent']['code'][:curDepth*2] != curNode['code'][:curDepth*2]:
            curNode = curNode['parent']
            curDepth = curNode['depth']
        if curNode['parent']:
            node['parent'] = curNode['parent']
            curNode['parent']['children'].append(node)
    curNode = node
    curDepth = depth

traverse(root, clearNode)
print json.dumps(root["children"])
