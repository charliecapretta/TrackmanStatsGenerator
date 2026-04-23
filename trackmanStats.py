import pandas as pd

#Change This!--------------------------------
df  = pd.read_csv('CSV_PATH')

def getWhiffPerc(dataframe):
    totalSwings = len(dataframe[dataframe['PitchCall'].isin(
        ['StrikeSwinging', 'InPlay', 'FoulBallNotFieldable', 'FoulBallFieldable'])])
    whiffPitches = len(dataframe[dataframe['PitchCall'] == 'StrikeSwinging'])
    whiffPercentage = (whiffPitches / totalSwings) * 100 if totalSwings > 0 else 0
    return whiffPercentage


def getSWPerc(dataframe):
    if dataframe.empty or 'PitchCall' not in dataframe.columns:
        return 0.0
    totalPitches = len(dataframe)
    swings = len(dataframe[dataframe['PitchCall'] == 'StrikeSwinging'])
    swPercentage = (swings / totalPitches) * 100 if totalPitches > 0 else 0.0
    return swPercentage


def getChasePerc(dataframe):
    outsideZone = ~((dataframe['PlateLocHeight'].between(1.5, 3.5)) & (dataframe['PlateLocSide'].between(-0.71, 0.71)))
    chaseSwings = dataframe[outsideZone & dataframe['PitchCall'].isin(
        ['StrikeSwinging', 'InPlay', 'FoulBallNotFieldable', 'FoulBallFieldable'])]
    totalChasePitches = len(dataframe[outsideZone])
    chasePercentage = (len(chaseSwings) / totalChasePitches) * 100 if totalChasePitches > 0 else 0
    return chasePercentage

def getZonePerc(dataframe):
    inZone = (dataframe['PlateLocHeight'].between(1.5, 3.5)) & (dataframe['PlateLocSide'].between(-0.71, 0.71))
    return (inZone.sum() / len(dataframe)) * 100


def avgPitchOfPA(dataframe):
    return round(dataframe['PitchofPA'].mean(), 2)

def getPA(dataframe):
    if 'PitchofPA' not in dataframe.columns:
        return 0
    return int((dataframe['PitchofPA'] == 1).sum())

def getxwOBA(df, xwobaData):
    return xwobaData.getXwOBA(df['ExitSpeed'], df['Angle'])

def getBatterXwOBA(batter_df, xwobaData):
    return xwobaData.get_batter_xwoba(batter_df)

def getBarrels(dataframe):
    return (dataframe['ExitSpeed'] > 95).sum()

#def get


def getIP(dataframe):
    # OutsOnPlay covers field outs (including double/triple plays) but NOT strikeouts
    field_outs = int(dataframe['OutsOnPlay'].sum()) if 'OutsOnPlay' in dataframe.columns else 0
    k_outs = len(dataframe[dataframe['KorBB'] == 'Strikeout']) if 'KorBB' in dataframe.columns else 0
    total_outs = field_outs + k_outs
    full_innings = total_outs // 3
    partial = total_outs % 3
    return f"{full_innings}.{partial}" if partial else str(full_innings)


def getHits(dataframe):
    return len(dataframe[dataframe['PlayResult'].isin(['Single', 'Double', 'Triple', 'HomeRun'])])


def getStrikeouts(dataframe):
    return len(dataframe[dataframe['KorBB'] == 'Strikeout'])


def getWalks(dataframe):
    return len(dataframe[dataframe['KorBB'] == 'Walk'])


def getHBP(dataframe):
    return len(dataframe[dataframe['PitchCall'] == 'HitByPitch'])


def getHR(dataframe):
    return len(dataframe[dataframe['PlayResult'] == 'HomeRun'])


def getRuns(dataframe):
    return int(dataframe['RunsScored'].sum()) if 'RunsScored' in dataframe.columns else 0


def getStrikePerc(dataframe):
    strikes = len(dataframe[dataframe['PitchCall'].isin([
        'StrikeCalled', 'StrikeSwinging',
        'FoulBallNotFieldable', 'FoulBallFieldable', 'InPlay'
    ])])
    total = len(dataframe)
    return round((strikes / total) * 100, 1) if total > 0 else 0.0


def getWhiffs(dataframe):
    return len(dataframe[dataframe['PitchCall'] == 'StrikeSwinging'])
