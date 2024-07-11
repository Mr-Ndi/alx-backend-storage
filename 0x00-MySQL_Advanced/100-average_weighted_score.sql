-- Create a stored procedure ComputeAverageWeightedScoreForUser
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    DECLARE average FLOAT;
    
    -- Calculate the total weighted score and total weight for the user
    SELECT SUM(c.score * p.weight), SUM(p.weight) INTO total_weighted_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = ComputeAverageWeightedScoreForUser.user_id;
    
    -- Calculate the average weighted score
    SET average = total_weighted_score / total_weight;
    
    -- Update the user's average_score
    UPDATE users
    SET average_score = average
    WHERE id = ComputeAverageWeightedScoreForUser.user_id;
END$$
DELIMITER ;