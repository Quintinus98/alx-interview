def canUnlockAll(boxes):
    if not boxes:
        return False

    num = len(boxes)
    visited = [False] * num
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < num and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)


if __name__ == "__main__":
    canUnlockAll()
