#  From https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

import re


class Solution:
    # This looks better than the refactored one.
    def simplify_path(self, path: str) -> str:
        consecutive_slashes_removed = re.sub(r"[/]+", "/", path)
        list_of_paths = list(filter(lambda x: x != "", re.split("/", consecutive_slashes_removed)))
        final_paths = []
        for _, el in enumerate(list_of_paths):
            if el == ".":
                continue
            elif el != "..":
                final_paths.append(el)
            elif len(final_paths) != 0:
                final_paths.pop()
        return f"/{'/'.join(final_paths)}"


    def simplify_path_refactored(self, path: str) -> str:
        single_dot_removed = re.sub(r'(?<=[/])\.(/|$)', '', path)
        consecutive_slashes_removed = re.sub(r'[/]+', '/', single_dot_removed)
        list_of_paths = list(filter(lambda x: x != "", re.split("/", consecutive_slashes_removed)))
        final_paths = []
        for _, el in enumerate(list_of_paths):
            if el != "..":
                final_paths.append(el)
            elif len(final_paths) != 0:
                final_paths.pop()
        return f"/{'/'.join(final_paths)}"
    


    # Double_dot_removed regex doesn't work as intended.
    def simplify_path_improved(self, path: str) -> str:
        single_dot_removed = re.sub(r'(?<=(/))\.(?=(/|$))', '', path)
        num_of_double_dot = len(re.findall(r'(?<=(/))\.\.(?=(/|$))', single_dot_removed))
        double_dot_removed = single_dot_removed
        for _ in range(num_of_double_dot):
            double_dot_removed = re.sub(r'(?<=(/))([a-zA-Z0-9_]*[/]+)?\.\.(?=(/|$))', '', double_dot_removed)
        consecutive_slashes_removed = re.sub(r'[/]+', '/', double_dot_removed)
        trailing_slash_removed = re.sub(r'/$', '', consecutive_slashes_removed)
        if len(trailing_slash_removed) == 0 or trailing_slash_removed[0] != "/":
            return f"/{trailing_slash_removed}"
        return trailing_slash_removed 


    def simplify_path_solution(self, path: str) -> str:
        sub_paths = path.split('/')
        stack = []

        for p in sub_paths:
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)
            

if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.simplify_path_solution("/home/") == "/home"
    assert s.simplify_path_solution("/../") == "/"
    assert s.simplify_path_solution("/home//foo/") == "/home/foo"
    assert s.simplify_path_solution("/a//./b//../../c/") == "/c"
    assert s.simplify_path_solution("/a//b////c/d//././/..") == "/a/b/c"
    assert s.simplify_path_solution("/.") == "/"
    print("Done!")
