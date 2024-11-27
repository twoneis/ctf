import random
import subprocess
import re
import os
from secret import flag

random.seed(os.urandom(8))

table = ['yellow', 'attack', 'costly', 'guitar', 'velvet', 'forbid', 'fluent', 'trophy', 'filter', 'flower', 'gossip', 'expose', 'forest', 'bitter', 'active', 'spider', 'empire', 'distant', 'famous', 'jungle', 'invent', 'breeze', 'height', 'golden', 'format', 'purple', 'luxury', 'beacon', 'center', 'ballot', 'debate', 'dream', 'hollow', 'future', 'combat', 'cousin', 'frozen', 'target', 'magnet', 'marble', 'bottle', 'absorb', 'permit', 'thrive', 'wonder', 'camera', 'monday', 'tennis', 'safari', 'donkey', 'output', 'cradle', 'medium', 'cloudy', 'simple', 'shield', 'whisky', 'remove', 'action', 'method', 'gather', 'elapse', 'burden', 'divide', 'harbor', 'basket', 'freeze', 'castle', 'garden', 'system', 'medal', 'supply', 'strain', 'bottom', 'annual', 'modern', 'vessel', 'whiten', 'poster', 'answer', 'wealth', 'afford', 'silent', 'origin', 'reward', 'gospel', 'design', 'friend', 'broken', 'expert', 'cargo', 'glance', 'finish', 'puzzle', 'bright', 'circle', 'margin', 'prince', 'normal', 'bounce', 'rescue', 'assist', 'tender', 'hungry', 'rotate', 'silver', 'screen', 'shadow', 'bishop', 'relate', 'school', 'absent', 'verify', 'oxygen', 'branch', 'candle', 'insane', 'stable', 'tunnel', 'energy', 'museum', 'stream', 'runner', 'humble', 'credit', 'submit', 'crunch', 'sunset', 'pillow', 'advice', 'safety', 'remind', 'expand', 'source', 'proton', 'honest', 'gallon', 'casual', 'ribbon', 'repeat', 'beyond', 'fabric', 'wander', 'button', 'cheese', 'author', 'affect', 'danger', 'master', 'jacket', 'remark', 'vision', 'planet', 'fiscal', 'gravel', 'unique', 'vacuum', 'market', 'prison', 'effort', 'animal', 'poison', 'anchor', 'canyon', 'pocket', 'laptop', 'temple', 'income', 'desire', 'reason', 'bridge', 'launch', 'artist', 'cattle', 'palace', 'hunter', 'pursue', 'pencil', 'random', 'shrink', 'sprint', 'cancel', 'banner']
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789_{}'

key = {}
for c in alphabet:
    while True:
        word = random.choice(table)
        if word not in key.values():
            key[c] = word
            break
print(f"{key = }")

flag = " ".join(map(lambda x: key[x], flag))

# take output of debug test running main function
"""
#[test]
fun main() {
    use std::debug;

    let input: vector<u8> = b"FLAG";
    let compressed: vector<u8> = compress(input);
    debug::print(&compressed);
}
"""

print(f"{out = }")
