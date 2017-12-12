s = ''
sure = True
with open("./platforms/ios/优先队列/Classes/MainViewController.m") as f:
    for l in f:
        s += l
        if l.startswith('@implementation MainViewController'):
            s += '''- (BOOL)prefersStatusBarHidden {
    return YES;
}
            '''
        elif l.startswith('- (BOOL)prefersStatusBarHidden'):
            sure = False
            break
if sure:
    with open("./platforms/ios/优先队列/Classes/MainViewController.m","w") as f:
        f.write(s)
print('preprocess success')
