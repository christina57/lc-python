"""

588. Design In-Memory File System

Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

Example:
Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
Output:
[null,[],null,null,["a"],"hello"]
Explanation:
filesystem
Note:
You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.

"""

class FileSystem(object):

    def __init__(self):
        self.root = Node("", True)
        self.contents = {}
    
    def findByPath(self, path, getDir):
        paths = path.split("/")
        cur = self.root
        if getDir:
            paths = paths[:-1]
        for p in paths:
            if p != "":
                cur = cur.sub[p]
        return cur
        
    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        cur = self.findByPath(path, False)
        if cur.isDirectory:
            return sorted(cur.sub.keys())
        else:
            return [cur.name]
        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        paths = path.split("/")
        cur = self.root
        for p in paths:
            if p != "":
                if p not in cur.sub:
                    cur.sub[p] = Node(p, True)
                cur = cur.sub[p]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        dir = self.findByPath(filePath, True)
        file = filePath[filePath.rindex("/")+1:]
        if file not in dir.sub:
            dir.sub[file] = Node(file, False)
            
        if file in self.contents:
            self.contents[file] = self.contents[file] + content
        else:
            self.contents[file] = content
            

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        cur = self.findByPath(filePath, False)
        if cur.name in self.contents:
            return self.contents[cur.name]
        else:
            return ""
            
class Node(object):
    def __init__(self, name, isDirectory):
        self.sub = {}
        self.name = name
        self.isDirectory = isDirectory

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)