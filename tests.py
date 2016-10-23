from models import BigramModel, ClusterModel

# Test
print '--- TESTING USER SIMULATION ---\n'

# Bigram Model
print '\n[BIGRAM MODEL]\n'

userSimulation = BigramModel()

print 'Recording \'fwd\' for \'fwd-inst\''
userSimulation.recordAction('fwd', 'fwd-inst')
print 'Recording \'back\' for \'fwd-inst\''
userSimulation.recordAction('back', 'fwd-inst')
print 'Recording \'left\' for \'fwd-inst\''
userSimulation.recordAction('left', 'fwd-inst')
print 'Recording \'left\' for \'fwd-inst\''
userSimulation.recordAction('left', 'fwd-inst')
print 'Recording \'right\' for \'fwd-inst\''
userSimulation.recordAction('right', 'fwd-inst')

print 'Recording \'fwd\' for \'back-inst\''
userSimulation.recordAction('fwd', 'back-inst')
print 'Recording \'back\' for \'back-inst\''
userSimulation.recordAction('back', 'back-inst')

print ''

print 'User Actions List: ', userSimulation.getUserActions()
print 'System Actions List: ', userSimulation.getSystemActions()

print ''

for systemAction in userSimulation.getSystemActions():
    for userAction in userSimulation.getUserActions():
        print 'Probability of \'%s\' for \'%s\': %f' % (userAction, systemAction, userSimulation.getProbability(userAction, systemAction))

print ''

print 'Predicted user action for \'fwd-inst\': ', userSimulation.getPredictedUserAction('fwd-inst')
print 'Predicted user action for \'back-inst\': ', userSimulation.getPredictedUserAction('back-inst')

# Cluster Model
print '\n[CLUSTER MODEL]\n'

userSimulation = ClusterModel()

print 'Recording \'fwd\' for \'fwd-inst\''
userSimulation.recordAction('fwd', 'fwd-inst')
print 'Recording \'back\' for \'fwd-inst\''
userSimulation.recordAction('back', 'fwd-inst')
print 'Recording \'left\' for \'fwd-inst\''
userSimulation.recordAction('left', 'fwd-inst')
print 'Recording \'left\' for \'fwd-inst\''
userSimulation.recordAction('left', 'fwd-inst')
print 'Recording \'right\' for \'fwd-inst\''
userSimulation.recordAction('right', 'fwd-inst')

print 'Recording \'fwd\' for \'back-inst\''
userSimulation.recordAction('fwd', 'back-inst')
print 'Recording \'back\' for \'back-inst\''
userSimulation.recordAction('back', 'back-inst')

print 'Recording \'fwd\' for \'left-inst\''
userSimulation.recordAction('fwd', 'left-inst')
print 'Recording \'back\' for \'left-inst\''
userSimulation.recordAction('back', 'left-inst')
print 'Recording \'left\' for \'left-inst\''
userSimulation.recordAction('left', 'left-inst')
print 'Recording \'left\' for \'left-inst\''
userSimulation.recordAction('left', 'left-inst')
print 'Recording \'right\' for \'left-inst\''
userSimulation.recordAction('right', 'left-inst')

print 'Recording \'fwd\' for \'right-inst\''
userSimulation.recordAction('fwd', 'right-inst')
print 'Recording \'back\' for \'right-inst\''
userSimulation.recordAction('back', 'right-inst')
print 'Recording \'left\' for \'right-inst\''
userSimulation.recordAction('left', 'right-inst')
print 'Recording \'right\' for \'right-inst\''
userSimulation.recordAction('right', 'right-inst')
print 'Recording \'right\' for \'right-inst\''
userSimulation.recordAction('right', 'right-inst')

print ''

print 'User Actions List: ', userSimulation.getUserActions()
print 'System Actions List: ', userSimulation.getSystemActions()

print ''

for systemAction in userSimulation.getSystemActions():
    for userAction in userSimulation.getUserActions():
        print 'Probability of \'%s\' for \'%s\': %f' % (userAction, systemAction, userSimulation.getProbability(userAction, systemAction))

print ''

for systemAction in userSimulation.getSystemActions():
    print 'Predicted user action for \'%s\': %s' % (systemAction, userSimulation.getPredictedUserAction(systemAction))

print ''

print 'Clusters: ', userSimulation.getClusters()
