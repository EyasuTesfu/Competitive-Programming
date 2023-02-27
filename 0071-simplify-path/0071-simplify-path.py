class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split("/")
        
        # pushing start to escape a previous path declarator
        start = 0
        while directory[start] == "..":
            start += 1
            
        # copying the directories based on rule
        copy_directory = [""]
        for i in range(start, len(directory)):
            if directory[i] == "." or directory[i] == "":
                continue
            if directory[i] == "..":
                if len(copy_directory) > 1:
                    copy_directory.pop()
            else:
                copy_directory.append(directory[i])
        if len(copy_directory) <= 1:
            return "/"
        return "/".join(copy_directory)